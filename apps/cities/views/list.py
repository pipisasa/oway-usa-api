from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.cities.models import City
from apps.cities.serializers import ListCitySerializer


class ListCityAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCitySerializer
    queryset = City.objects.all()