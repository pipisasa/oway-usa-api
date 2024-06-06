from datetime import timedelta

from django.db.models import Sum
from django.db.models.functions import TruncDay, TruncHour
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.warehouses.models import Status, WarehouseProduct
from ..filter_helper import in_filters
from apps.shared.views import FilterHelper


class StaticsWarehousePaidAPI(APIView, FilterHelper):
    permission_classes = [AllowAny]

    def _filter_queryset(self, request, queryset):
        query_params = request.query_params.copy()

        q_objects = self.build_filters(
            query_params=query_params,
            simple_filters=[],
            in_filters=in_filters,
            boolean_filters=[],
            range_filters=[],
            text_search_filters=[],
        )
        queryset = queryset.filter(q_objects)
        return queryset

    def get_queryset_filter(self):
        delivered_status = Status.objects.get(name="Доставлено")
        queryset = Warehouse.objects.filter(status=delivered_status)
        filtered_queryset = self._filter_queryset(self.request, queryset)
        return filtered_queryset

    def aggregate_by_days(self, start_date, end_date, data_dict):
        entries = self.get_queryset_filter().filter(
            created_at__range=(start_date, end_date)
        ).annotate(day=TruncDay('created_at')).values('day').annotate(total=Sum('price')).order_by('day')

        for entry in entries:
            day = entry['day'].date().strftime('%Y-%m-%d')
            data_dict[day] = entry['total']

    def get(self, request):
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

        today_hours = self.get_queryset_filter().filter(
            created_at__gte=start_of_today
        ).annotate(hour=TruncHour('created_at')).values('hour').annotate(total=Sum('price')).order_by('hour')

        for entry in today_hours:
            hour = entry['hour'].hour
            today_data[str(hour)] = entry['total']

        self.aggregate_by_days(start_of_week, now, week_data)
        self.aggregate_by_days(start_of_month, now, month_data)

        result = {
            'today': today_data,
            'week': week_data,
            'month': month_data
        }
        return Response(result, status=status.HTTP_200_OK)
