from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User

from apps.users.serializers import ProfileSerializer, ProfileUpdateSerializer


class ProfileDetailAPI(APIView):
    permission_classes = [IsAdminUser]
    serializer_class = ProfileSerializer
    update_serializer_class = ProfileUpdateSerializer

    def get_user(self, id):
        user = get_object_or_404(User, id=id)
        return user

    def process_update(self, request, id, partial):
        user = self.get_user(id)
        serializer = self.update_serializer_class(user, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        user = self.get_user(id)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request, id):
        return self.process_update(request, id, True)

    def put(self, request, id):
        return self.process_update(request, id, False)