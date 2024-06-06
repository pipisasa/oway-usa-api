from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.my_warehouse.models import MyWarehouse
from apps.my_warehouse.serializers import MyWarehouseCreateUpdateSerializer


class MyWarehouseAddView(APIView):
    serializer_class = MyWarehouseCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        user = request.user
        my_warehouse = MyWarehouse.objects.create(
            user=user,
            warehouse=data['warehouse'],
            tracking_number=data['tracking_number'],
            courier_service=data['courier_service'],
            comments=data['comments'],
        )
        my_warehouse.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
