from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.warehouses.models import Status, Warehouse


class StaticsWarehouseDeliveredAPI(APIView):
    permission_classes = [AllowAny]

    def fill_data_for_period(self, period_dict, start_date, period, delivered_status):
        for day, _ in period_dict.items():
            day_start = timezone.datetime.strptime(day, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            day_end = day_start + timedelta(days=1)
            count = Warehouse.objects.filter(
                status=delivered_status, created_at__range=(day_start, day_end)
            ).count()
            period_dict[day] = count

    def get(self, request):
        delivered_status = Status.objects.get(name="Доставлено")

        now = timezone.now()

        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)

        today = {str(hour): 0 for hour in range(24)}
        week = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.weekday(), -1, -1)}
        month = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.day - 1, -1, -1)}

        for hour in range(24):
            hour_start = start_of_today + timedelta(hours=hour)
            hour_end = hour_start + timedelta(hours=1)
            count = Warehouse.objects.filter(
                status=delivered_status, created_at__range=(hour_start, hour_end)
            ).count()
            today[str(hour)] = count

        self.fill_data_for_period(week, start_of_today - timedelta(days=now.weekday()), 'week', delivered_status)
        self.fill_data_for_period(month, start_of_today.replace(day=1), 'month', delivered_status)

        result = {
            'today': today,
            'week': week,
            'month': month
        }
        return Response(result, status=status.HTTP_200_OK)
