from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.contacts.models import Contact
from apps.contacts.serializers import ContactCreateSerializer


class CreateContactAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = ContactCreateSerializer

    @swagger_auto_schema(
        operation_summary="Create Contact",
        request_body=ContactCreateSerializer,
        responses={
            201: "Successfully created",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden"
        }
    )
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
