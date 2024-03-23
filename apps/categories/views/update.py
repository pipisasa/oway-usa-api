from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.categories.models import Category
from apps.categories.serializers.categories_serializer import UpdateCategorySerializer


class UpdateCategoryAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = UpdateCategorySerializer
    model_class = Category

    def process_request(self, request, id, partial):
        instance = self.model_class.objects.filter(id=id).first()
        data = request.data
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance, data=data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        instance = self.model_class.objects.filter(id=id).first()
        if not instance:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        return self.process_request(request, id, False)

    def patch(self, request, id):
        return self.process_request(request, id, True)

