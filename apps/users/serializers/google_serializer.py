from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User


class LoginGoogleSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255, required=True)


class ProfileGoogleAccountSerializer(serializers.Serializer):
    email = serializers.CharField()

    def validate(self, data):
        user = None
        if '@' in data['email']:
            user = User.objects.filter(email=data['email']).first()

        refresh = RefreshToken.for_user(user)
        return {
            'id': user.id,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }