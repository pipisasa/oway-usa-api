from datetime import timedelta

from django.db.models import Sum
from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.warehouses.models import Status, WarehouseProduct
from ..filter_helper import in_filters
from apps.shared.views import FilterHelper


class StaticsWarehouseWeightAPI(APIView, FilterHelper):
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
        queryset = WarehouseProduct.objects.filter(status=delivered_status)
        filtered_queryset = self._filter_queryset(self.request, queryset)
        return filtered_queryset

    def aggregate_weight_by_intervals(self, start, end, interval='hourly'):
        aggregates = []
        current = start
        while current < end:
            next_interval = current + (timedelta(hours=1) if interval == 'hourly' else timedelta(days=1))
            weight = self.get_queryset_filter().filter(
                created_at__range=(current, next_interval)
            ).aggregate(total_weight=Sum('weight'))['total_weight'] or 0

            if interval == 'hourly':
                aggregates.append((current.strftime('%H:%M'), weight))
            else:
                aggregates.append((current.strftime('%Y-%m-%d'), weight))

            current = next_interval
        return aggregates

    def get(self, request):

        now = timezone.now()

        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)

        today = {str(hour): 0 for hour in range(24)}
        week = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.weekday(), -1, -1)}
        month = {(start_of_today - timedelta(days=i)).strftime('%Y-%m-%d'): 0 for i in range(now.day - 1, -1, -1)}

        for hour in range(24):
            hour_start = start_of_today + timedelta(hours=hour)
            hour_end = hour_start + timedelta(hours=1)
            weight = self.get_queryset_filter().filter(
                created_at__range=(hour_start, hour_end)
            ).aggregate(Sum('weight'))['weight__sum'] or 0
            today[str(hour)] = weight

        for period in ['week', 'month']:
            for day in eval(period).keys():
                day_start = timezone.datetime.strptime(day, '%Y-%m-%d')
                day_end = day_start + timedelta(days=1)
                weight = self.get_queryset_filter().filter(
                    created_at__range=(day_start, day_end)
                ).aggregate(Sum('weight'))['weight__sum'] or 0
                eval(period)[day] = weight

        result = {
            'today': today,
            'week': week,
            'month': month
        }
        return Response(result, status=status.HTTP_200_OK)
