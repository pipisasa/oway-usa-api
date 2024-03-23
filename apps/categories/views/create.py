from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from apps.categories.models import Category
from apps.categories.serializers import BaseCategorySerializer


class CreateCategoryAPI(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = BaseCategorySerializer
    queryset = Category.objects.all()