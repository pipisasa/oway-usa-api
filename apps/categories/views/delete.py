from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.categories.models import Category


class DeleteCategoryAPI(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id):
        category = Category.objects.filter(id=id).first()
        if category:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
