from rest_framework import serializers

from apps.logos.models import Logo


class LogoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logo
        fields = "__all__"
