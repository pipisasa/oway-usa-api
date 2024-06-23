from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


from apps.contacts.models import Contact
from apps.contacts.serializers import ContactListSerializer


class ContactDetailAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = ContactListSerializer

    @swagger_auto_schema(
        operation_summary="Get item",
        responses={
            200: ContactListSerializer()
        }
    )
    def get(self, request, id):
        item_instance = get_object_or_404(Contact, id=id)
        serializer = ContactListSerializer(item_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)