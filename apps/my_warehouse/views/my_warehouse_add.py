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
        data = request.data.copy()
        user = request.user
        if user.is_admin is False:
            data['user'] = user.id
        else:
            if data.get('user', None) is None:
                data['user'] = user.id
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
