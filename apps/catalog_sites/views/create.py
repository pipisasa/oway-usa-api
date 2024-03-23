from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.catalog_sites.serializers import CatalogSiteSerializer


class CreateCatalogSiteAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = CatalogSiteSerializer

    @swagger_auto_schema(
        request_body=CatalogSiteSerializer,
        responses={201: CatalogSiteSerializer})
    def post(self, request, *args, **kwargs):
        serializer = CatalogSiteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)