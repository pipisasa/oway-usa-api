from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.warehouses.models import WarehouseProduct


class DeleteWarehouseProductAPI(APIView):
    permission_classes = [IsAdminUser]

    def delete(self, request, id, *args, **kwargs):

        if id != 'all':
            warehouse_product_instance = get_object_or_404(WarehouseProduct, pk=int(id))
        else:
            warehouse_product_instance = WarehouseProduct.objects.all()

        warehouse_product_instance.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
