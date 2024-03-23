from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog_sites.models import CatalogSite


class DeleteCatalogSitesAPI(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        category = CatalogSite.objects.filter(id=id).first()
        if category:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
