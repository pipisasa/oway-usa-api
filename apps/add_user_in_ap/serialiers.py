from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from apps.users.models import User


class AddUserSerializer(serializers.ModelSerializer):
    front_image = serializers.ImageField(required=False)
    back_image = serializers.ImageField(required=False)
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'password2', 'front_image',
                  'back_image']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs: dict):
        """
        Validates password match and normalizes email before saving.
        Args:
            attrs (dict): Dictionary containing user input data.
        Returns:
            dict: Validated and normalized data.
        Raises:
            serializers.ValidationError: If passwords do not match or email is already in use.
        """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        attrs['email'] = attrs['email'].lower()
        if User.objects.filter(email=attrs['email']).exists():
            raise ValidationError({"email": "This email is already in use."})
        return attrs
