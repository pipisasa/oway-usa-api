from django.urls import path

from apps.notifications.views.check_all_notifications import CheckAllNotificationsAPIView
from apps.notifications.views.create_notification import CreateNotificationAPIView
from apps.notifications.views.delete_notification import DeleteNotificationAPIView
from apps.notifications.views.my_notifications_list import UserNotificationsListAPIView
from apps.notifications.views.notification_detail import MailBoxDetailAPIView
from apps.notifications.views.notification_list import NotificationsListAPIView
from apps.notifications.views.update_notification import UpdateNotificationsAPIView

urlpatterns = [
    path('create_notification/', CreateNotificationAPIView.as_view(), name='create_notification'),
    path('my_notification/', UserNotificationsListAPIView.as_view(), name='my_notification'),
    path('list/', NotificationsListAPIView.as_view(), name='list'),
    path('check_all/', CheckAllNotificationsAPIView.as_view(), name='check_all'),
    path('notification_detail/<int:pk>/', MailBoxDetailAPIView.as_view(), name='notification_detail'),
    path('update_notification/<int:pk>/', UpdateNotificationsAPIView.as_view(), name='update_notification'),
    path('delete_notification/<int:pk>/', DeleteNotificationAPIView.as_view(), name='delete_notification'),
]
