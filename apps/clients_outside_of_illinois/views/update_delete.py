from rest_framework import generics, permissions

from apps.clients_outside_of_illinois import model, serializers


class ClientRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = model.OutsideOfIllinois.objects.all()
    serializer_class = serializers.ClientSerializer
    permission_classes = [permissions.IsAdminUser]
