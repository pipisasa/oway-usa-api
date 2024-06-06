from rest_framework import generics, permissions

from apps.logos.models import Logo
from apps.logos.serializers import LogoSerializer


class LogoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    permission_classes = [permissions.IsAdminUser]

