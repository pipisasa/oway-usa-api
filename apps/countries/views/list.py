from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.countries.models import Country
from apps.countries.serializers import ListCountrySerializer


class ListCountryAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCountrySerializer
    queryset = Country.objects.all()