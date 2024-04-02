from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.shared.utils.mailing.send_activation_code import send_activation_code
from apps.users.serializers import SignUpSerializer


class AddUserForAdminAPIView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['is_active'] = True

        serializer = self.serializer_class(data=mutable_data)
        if serializer.is_valid():
            user = serializer.save()
            user.create_activation_code()
            send_activation_code(user=user)
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
