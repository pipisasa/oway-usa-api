from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User


class DeleteUserAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Delete User API",
        operation_description="id: delete a User",
        responses={
            204: "User deleted successfully",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def put(self, request, *args, **kwargs):
        ids = request.data.get("ids")

        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)

        if ids != 'all':
            ids = map(int, ids)
            instances = User.objects.filter(pk__in=ids)
            if not instances.exists():
                return Response({"error": "Objects not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            instances = User.objects.all()

        instances.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
