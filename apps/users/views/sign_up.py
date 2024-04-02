from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.shared.utils.mailing.send_activation_code import send_activation_code
from apps.users.models import User
from apps.users.serializers import SignUpSerializer


class SignUpAPIView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = User.objects.create(
                phone_number=data.get('phone_number'),
                email=data.get('email'),
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                password=data.get('password')
            )
            user.save()
            user.create_activation_code()
            send_activation_code(user=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
