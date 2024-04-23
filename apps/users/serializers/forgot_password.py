from rest_framework import serializers

from apps.shared.utils.mailing.forgot_password import send_email_change_password
from apps.users.models import User


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, email):
        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError({"error_code": "USER_DOESNT_EXIST"})
        return user.email

    def send_verification_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        send_email_change_password(user)


class ForgotPasswordCompleteSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()
    password = serializers.CharField(min_length=6)
    password2 = serializers.CharField(min_length=6)

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        pass1 = attrs.get('password')
        pass2 = attrs.get('password2')
        user = User.objects.filter(email=email).first()
        if not user:
            raise serializers.ValidationError({"error_code": "USER_DOESNT_EXIST"})
        if pass1 != pass2:
            raise serializers.ValidationError({"error_code": "PASSWORDS_DO_NOT_MATCH"})
        if user.activation_code != code:
            raise serializers.ValidationError({"error_code": "INCORRECT_ACTIVATION_CODE"})
        return super().validate(attrs)

    def set_new_password(self):
        email = self.validated_data.get('email')
        password = self.validated_data.get('password')
        user = User.objects.get(email=email)
        user.password = password
        user.save()