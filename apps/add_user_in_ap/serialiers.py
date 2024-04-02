from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'unique_id', 'first_name', 'last_name', 'phone_number', 'email', 'avatar', 'address', 'is_active', 'is_superuser', 'is_admin', 'is_staff', 'is_banned', 'created_at')
