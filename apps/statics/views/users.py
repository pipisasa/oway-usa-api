from datetime import timedelta

from django.utils import timezone
from rest_framework import status
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.models import User


class StaticsUserAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        now = timezone.now()

        start_of_today = now.replace(hour=0, minute=0, second=0, microsecond=0)
        start_of_week = start_of_today - timedelta(days=start_of_today.weekday())
        start_of_month = start_of_today.replace(day=1)

        hourly_stats = {}
        for hour in range(24):
            hour_start = start_of_today + timedelta(hours=hour)
            hour_end = hour_start + timedelta(hours=1)
            hour_users = User.objects.filter(created_at__range=(hour_start, hour_end)).count()
            hourly_stats[hour] = hour_users

        weekly_stats = {}
        for i in range((now - start_of_week).days + 1):
            day = start_of_week + timedelta(days=i)
            next_day = day + timedelta(days=1)
            count = User.objects.filter(created_at__range=(day, next_day)).count()
            weekly_stats[day.strftime('%Y-%m-%d')] = count

        monthly_stats = {}
        for i in range(now.day):
            day = start_of_month + timedelta(days=i)
            next_day = day + timedelta(days=1)
            count = User.objects.filter(created_at__range=(day, next_day)).count()
            monthly_stats[day.strftime('%Y-%m-%d')] = count

        result = {
            'today': hourly_stats,
            'week': weekly_stats,
            'month': monthly_stats
        }
        return Response(result, status=status.HTTP_200_OK)
