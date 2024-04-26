from rest_framework import serializers

from apps.clients_outside_of_illinois import model


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = model.OutsideOfIllinois
        fields = '__all__'
