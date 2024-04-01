from rest_framework import serializers
from apps.catalog_sites.models import CatalogSite
from apps.categories.serializers import DetailCategorySerializer
from apps.countries.serializers import DetailCountrySerializer


class CatalogSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogSite
        fields = '__all__'


class CatalogSiteListSerializer(CatalogSiteSerializer):
    country = DetailCountrySerializer()
    category = DetailCategorySerializer()
