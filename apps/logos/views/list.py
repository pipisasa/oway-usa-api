from rest_framework import generics

from apps.logos.models import Logo
from apps.logos.serializers import LogoSerializer


class LogoListView(generics.ListAPIView):
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer

