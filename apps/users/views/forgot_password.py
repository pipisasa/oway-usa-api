from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

from apps.users.serializers import ForgotPasswordSerializer, ForgotPasswordCompleteSerializer


class ForgotPasswordSendActivationCodeView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        serializer = ForgotPasswordSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.send_verification_code()
            return Response('Вам выслан код верификации', status=status.HTTP_200_OK)


class ForgotPasswordCompleteView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        data = request.data
        serializer = ForgotPasswordCompleteSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.set_new_password()
            return Response('Пароль успешно обновлён', status=status.HTTP_200_OK)