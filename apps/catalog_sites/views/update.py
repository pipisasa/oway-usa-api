from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from apps.catalog_sites.models import CatalogSite
from apps.catalog_sites.serializers import CatalogSiteSerializer


class UpdateCatalogSiteAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = CatalogSiteSerializer
    model_class = CatalogSite

    @swagger_auto_schema(request_body=CatalogSiteSerializer, responses={200: CatalogSiteSerializer()})
    def put(self, request, id):
        return self.process_request(request, id, False)

    @swagger_auto_schema(request_body=CatalogSiteSerializer, responses={200: CatalogSiteSerializer()})
    def patch(self, request, id):
        return self.process_request(request, id, True)

    def process_request(self, request, id, partial):
        instance = self.model_class.objects.filter(id=id).first()
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
