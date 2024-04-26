from rest_framework.response import Response

from apps.shared.views.list_view import ListAPIView
from apps.clients_outside_of_illinois import serializers, model

from rest_framework import permissions, status


class ClientsOutsideOfIllinoisListView(ListAPIView):
    permission_classes = [permissions.IsAdminUser]

    def get_serializer_class(self):
        return serializers.ClientSerializer

    def get_queryset(self):
        return model.OutsideOfIllinois.objects.all()

    def get(self, request):
        queryset = self.get_queryset()
        base_response, _ = self.get_base_response(queryset, request)

        response_data = {
            **base_response,
        }

        return Response(response_data, status=status.HTTP_200_OK)
