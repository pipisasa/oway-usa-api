from rest_framework import serializers

from apps.users.models import PassportFront, PassportBack


class PassportFrontSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportFront
        fields = ['front_image']


class PassportBackSerializer(serializers.ModelSerializer):
    class Meta:
        model = PassportBack
        fields = ['back_image']