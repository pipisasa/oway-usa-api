from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.categories.models import Category
from apps.categories.serializers import ListCategorySerializer


class ListCategoryAPI(ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = ListCategorySerializer
    queryset = Category.objects.all()