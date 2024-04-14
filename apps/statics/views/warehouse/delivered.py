from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.warehouses.models import Status, Warehouse
from apps.shared.views.filter_helpers import FilterHelper
from ..filter_helper import in_filters


class StaticsWarehouseDeliveredAPI(APIView, FilterHelper):
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

    def fill_data_for_period(self, period_dict, start_date, period):
        for day, _ in period_dict.items():
            day_start = timezone.datetime.strptime(day, '%Y-%m-%d').replace(tzinfo=timezone.utc)
            day_end = day_start + timedelta(days=1)
            count = self.get_queryset_filter().filter(
                created_at__range=(day_start, day_end)
            ).count()
            period_dict[day] = count

    def get(self, request):
        now = timezone.now()

        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)

        today = {str(hour): 0 for hour in range(24)}
        week = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.weekday(), -1, -1)}
        month = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.day - 1, -1, -1)}

        for hour in range(24):
            hour_start = start_of_today + timedelta(hours=hour)
            hour_end = hour_start + timedelta(hours=1)
            count = self.get_queryset_filter().filter(
                created_at__range=(hour_start, hour_end)
            ).count()
            today[str(hour)] = count

        self.fill_data_for_period(week, start_of_today - timedelta(days=now.weekday()), 'week')
        self.fill_data_for_period(month, start_of_today.replace(day=1), 'month')

        result = {
            'today': today,
            'week': week,
            'month': month
        }
        return Response(result, status=status.HTTP_200_OK)
