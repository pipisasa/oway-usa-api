from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import ProfileSerializer, ProfileUpdateSerializer


class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    update_serializer_class = ProfileUpdateSerializer

    def get_user(self, request):
        user = request.user
        return user

    def process_update(self, request, partial):
        user = self.get_user(request=request)
        serializer = self.update_serializer_class(user, data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        user = self.get_user(request)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request):
        return self.process_update(request, True)

    def put(self, request):
        return self.process_update(request, False)