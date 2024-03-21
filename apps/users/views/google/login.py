from django.db import transaction
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

from apps.users.models import User
from apps.users.serializers import LoginGoogleSerializer, SignInSerializer, ProfileGoogleAccountSerializer

from google.auth.transport import requests as google_requests
from google.oauth2 import id_token


class GoogleLoginAPI(APIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginGoogleSerializer

    def get_token_from_request_data(self, data):
        token = data.get("token")
        if not token:
            raise AuthenticationFailed(detail="Token not provided", code=status.HTTP_400_BAD_REQUEST)
        return token

    def verify_google_token(self, token):
        try:
            return id_token.verify_oauth2_token(token, google_requests.Request())
        except ValueError:
            raise AuthenticationFailed(detail="Bad token Google", code=status.HTTP_403_FORBIDDEN)

    def process_google_login(self, info_user):
        with transaction.atomic():
            user_email = info_user.get("email")
            user = User.objects.filter(email=user_email).first() if user_email else None

            if user:
                if user.is_active:
                    login_serializer = ProfileGoogleAccountSerializer(data={"email": user.email})
                    login_serializer.is_valid(raise_exception=True)
                    return Response(login_serializer.validated_data, status=status.HTTP_200_OK)
                return Response({'error_code': 'USER_NOT_ACTIVE'}, status=status.HTTP_401_UNAUTHORIZED)

            user = User.objects.create(
                email=info_user["email"],
                first_name=info_user.get("given_name", ""),
                last_name=info_user.get("family_name", ""),
            )
            user.is_active = True
            user.save()
            login_serializer = ProfileGoogleAccountSerializer(data={"email": user.email})
            if login_serializer.is_valid():
                return Response(login_serializer.validated_data, status=status.HTTP_200_OK)
            return Response(login_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(
        operation_description="Login Goole",
        request_body=LoginGoogleSerializer,
        responses={200: openapi.Response(description="Login Google successfully")}
    )
    def post(self, request):
        token = self.get_token_from_request_data(request.data)
        info_user = self.verify_google_token(token)
        return self.process_google_login(info_user)