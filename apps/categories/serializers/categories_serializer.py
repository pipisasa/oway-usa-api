from rest_framework import serializers

from apps.categories.models import Category

base_field = [
    'name',
    'codename',
    'icon'
]


class BaseCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = base_field


class ListCategorySerializer(BaseCategorySerializer):

    class Meta:
        model = Category
        fields = ["id"] + base_field


class UpdateCategorySerializer(BaseCategorySerializer):

    class Meta:
        model = Category
        fields = ["id"] + base_field
