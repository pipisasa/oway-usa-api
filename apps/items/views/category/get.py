from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.items.models import Category
from apps.items.serializers import CategoryListSerializer


class CategoryDetailAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryListSerializer

    @swagger_auto_schema(
        operation_summary="Get Category",
        responses={
            200: CategoryListSerializer()
        }
    )
    def get(self, request, id):
        item_instance = get_object_or_404(Category, id=id)
        serializer = CategoryListSerializer(item_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)