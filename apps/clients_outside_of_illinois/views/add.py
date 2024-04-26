from rest_framework import generics

from apps.clients_outside_of_illinois import model
from apps.clients_outside_of_illinois import serializers


class AddClient(generics.CreateAPIView):
    queryset = model.OutsideOfIllinois.objects.all()
    serializer_class = serializers.ClientSerializer
