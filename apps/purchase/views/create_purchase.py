from rest_framework import generics, status, permissions
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.purchase import models
from apps.purchase import serializers


class CreatePurchase(generics.CreateAPIView):
    queryset = models.Purchase.objects.all()
    serializer_class = serializers.PurchaseCreateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = request.user

        request.data['user'] = user.id

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

