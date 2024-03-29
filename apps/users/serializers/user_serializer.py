from django.db import transaction
from rest_framework import serializers
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.generics import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

from apps.users.models import User, PassportFront, PassportBack

from .passport_serializer import PassportFrontSerializer, PassportBackSerializer


class SignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'password', 'password2']
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


class ActivationAccountSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

    def validate(self, data: dict):
        """
        Validate the email and activation code.
        This method checks if a user with the provided email address and activation code exists.
        Args:
            data (dict): The input data containing 'email' and 'code'.
        Returns:
            dict: The validated data.
        Raises:
            serializers.ValidationError: If no user is found with the provided email and activation code.
        """
        email = data.get('email')
        code = data.get('code')
        if not User.objects.filter(email=email, activation_code=code).exists():
            raise serializers.ValidationError('Пользователь не найден')
        return data

    def activate(self):
        """
        Activate the user account.
        This method activates the user account associated with the provided email address
        by setting the 'is_active' flag to True and clearing the activation code.
        Raises:
            User.DoesNotExist: If no user is found with the provided email address.
        """
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.is_active = True
        user.activation_code = ''
        user.save()


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data: dict):
        """
        Validates the provided user data.
        Args:
            data (dict): Dictionary containing data to be validated.
        Returns:
            dict: Dictionary containing user data and access tokens.
        Raises:
            serializers.ValidationError: If invalid data is provided.
        """
        email = data.get('email')
        password = data.get('password')

        user = self._get_user(email)
        self._validate_password(user, password)
        self._validate_user_active(user)

        refresh = self._create_refresh_token(user)
        return self._format_response(user, refresh)

    def _get_user(self, email: str):
        """
        Retrieves a user by their email.
        Args:
            email (str): User's email.
        Returns:
            MyUser: User object.
        Raises:
            Http404: If no user with the given email is found.
        """
        return get_object_or_404(User, email=email)

    def _validate_user_active(self, user: User):
        """
        Validates if the user is active.
        Args:
            user (MyUser): User object.
        Raises:
            exceptions.AuthenticationFailed: If the user is not active.
        """
        if not user.is_active:
            raise AuthenticationFailed(
                detail={'error_code': 'USER_NOT_ACTIVE'}
            )

    def _validate_password(self, user: User, password: str):
        """
        Validates the user's provided password.
        Args:
            user (MyUser): User object.
            password (str): Password provided by the user.
        Raises:
            serializers.ValidationError: If the password is incorrect.
        """
        print(password, user.password)
        if user.password!=password:
            raise serializers.ValidationError('Incorrect email or password')

    def _create_refresh_token(self, user: User):
        """
        Creates a refresh token for the user.
        Args:
            user (MyUser): User object.
        Returns:
            RefreshToken: Refresh token object.
        Raises:
            serializers.ValidationError: If unable to create the token.
        """
        try:
            refresh = RefreshToken.for_user(user)
        except Exception as e:
            raise serializers.ValidationError('Unable to create refresh token')

        return refresh

    def _format_response(self, user: User, refresh: RefreshToken):
        """
        Formats user data and tokens for the response.
        Args:
            user (MyUser): User object.
            refresh (RefreshToken): Refresh token object.
        Returns:
            dict: Dictionary containing user data and access tokens.
        """
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class ProfileSerializer(serializers.ModelSerializer):
    front_image = serializers.SerializerMethodField()
    back_image = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("id", "unique_id", "first_name", "last_name", "email", "avatar", "front_image", "back_image")

    def get_front_image(self, obj):
        try:
            passport_front = PassportFront.objects.get(user=obj)
            return PassportFrontSerializer(passport_front).data["front_image"]
        except PassportFront.DoesNotExist:
            return None

    def get_back_image(self, obj):
        try:
            passport_back = PassportBack.objects.get(user=obj)
            return PassportBackSerializer(passport_back).data["back_image"]
        except PassportBack.DoesNotExist:
            return None

    def update(self, instance, validated_data):
        front_image_data = validated_data.pop('front_image', None)
        back_image_data = validated_data.pop('back_image', None)

        instance = super().update(instance, validated_data)

        if front_image_data:
            if hasattr(instance, 'passportfront'):
                instance.passportfront.front_image = front_image_data
                instance.passportfront.save()
            else:
                PassportFront.objects.create(user=instance, front_image=front_image_data)

        if back_image_data:
            if hasattr(instance, 'passportback'):
                instance.passportback.back_image = back_image_data
                instance.passportback.save()
            else:
                PassportBack.objects.create(user=instance, back_image=back_image_data)

        return instance


class ProfileUpdateSerializer(serializers.ModelSerializer):
    front_image = serializers.ImageField(write_only=True)
    back_image = serializers.ImageField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "email", "avatar", "front_image", "back_image")

    def get_front_image(self, obj):
        try:
            passport_front = PassportFront.objects.get(user=obj)
            return PassportFrontSerializer(passport_front).data["front_image"]
        except PassportFront.DoesNotExist:
            return None

    def get_back_image(self, obj):
        try:
            passport_back = PassportBack.objects.get(user=obj)
            return PassportBackSerializer(passport_back).data["back_image"]
        except PassportBack.DoesNotExist:
            return None

    def update(self, instance, validated_data):
        front_image_data = validated_data.pop('front_image', None)
        back_image_data = validated_data.pop('back_image', None)

        instance = super().update(instance, validated_data)

        if front_image_data:
            if hasattr(instance, 'passportfront'):
                instance.passportfront.front_image = front_image_data
                instance.passportfront.save()
            else:
                PassportFront.objects.create(user=instance, front_image=front_image_data)

        if back_image_data:
            if hasattr(instance, 'passportback'):
                instance.passportback.back_image = back_image_data
                instance.passportback.save()
            else:
                PassportBack.objects.create(user=instance, back_image=back_image_data)

        return instance