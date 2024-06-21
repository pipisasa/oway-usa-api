from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User


class UpdateUserAPI(APIView):
    permission_classes = [IsAdminUser]

    @swagger_auto_schema(
        operation_summary="Update User API",
        operation_description="id: update a User",
        responses={
            200: "User update successfully",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def put(self, request, *args, **kwargs):
        ids = request.data.get("ids")
        query = request.query_params

        if not ids:
            return Response({"error": "No IDs provided"}, status=status.HTTP_400_BAD_REQUEST)
        users = User.objects.filter(pk__in=ids)
        is_admin = query.get("is_admin")

        if is_admin:
            users.update(is_admin=is_admin)

        return Response(status=status.HTTP_200_OK)
