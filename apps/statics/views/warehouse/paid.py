from datetime import timedelta

from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncHour
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.warehouses.models import Status, Warehouse


class StaticsWarehousePaidAPI(APIView):
    permission_classes = [AllowAny]

    @staticmethod
    def aggregate_by_days(start_date, end_date, data_dict, paid_status):
        entries = Warehouse.objects.filter(
            status=paid_status,
            created_at__range=(start_date, end_date)
        ).annotate(day=TruncDay('created_at')).values('day').annotate(total=Sum('price')).order_by('day')

        for entry in entries:
            day = entry['day'].date().strftime('%Y-%m-%d')
            data_dict[day] = entry['total']

    def get(self, request):
        paid_status = Status.objects.get(name="Доставлено")
        now = timezone.now()
        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_of_week = start_of_today - timedelta(days=start_of_today.weekday())
        start_of_month = start_of_today.replace(day=1)

        today_data = {str(hour): 0 for hour in range(24)}

        week_data = {}
        month_data = {}

        end_of_week = start_of_week + timedelta(days=6)
        week_data = {(start_of_week + timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in
                     range((end_of_week - start_of_week).days + 1)}

        days_in_month = (start_of_month + timedelta(days=31)).replace(day=1) - timedelta(days=1)
        end_of_month = start_of_month + timedelta(days=days_in_month.day - 1)
        month_data = {(start_of_month + timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in
                      range((end_of_month - start_of_month).days + 1)}

        today_hours = Warehouse.objects.filter(
            status=paid_status, created_at__gte=start_of_today
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(total=Sum('price')).order_by('hour')

        for entry in today_hours:
            hour = entry['hour'].hour
            today_data[str(hour)] = entry['total']

        self.aggregate_by_days(start_of_week, now, week_data, paid_status)
        self.aggregate_by_days(start_of_month, now, month_data, paid_status)

        result = {
            'today': today_data,
            'week': week_data,
            'month': month_data
        }
        return Response(result, status=status.HTTP_200_OK)
