from rest_framework import permissions, generics

from apps.logos.models import Logo
from apps.logos.serializers import LogoSerializer


class LogoAddView(generics.CreateAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer
    permission_classes = [permissions.IsAdminUser]

