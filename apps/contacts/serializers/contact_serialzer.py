from rest_framework import serializers

from apps.contacts.models import Contact


class ContactCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'


class ContactListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'