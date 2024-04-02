from django.urls import path

from apps.add_user_in_ap.views import AddUserForAdminAPIView

urlpatterns = [
    path('add/', AddUserForAdminAPIView.as_view(), name="add_user"),
]
