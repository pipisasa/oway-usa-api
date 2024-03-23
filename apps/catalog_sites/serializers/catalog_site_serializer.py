from rest_framework import serializers
from apps.catalog_sites.models import CatalogSite


class CatalogSiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CatalogSite
        fields = '__all__'