from django.urls import path

from apps.add_user_in_ap.views import AddUserForAdminAPIView, UserListAPIView, UserSearchAPIView

urlpatterns = [
    path('add/', AddUserForAdminAPIView.as_view(), name="add_user"),
    path('list/', UserListAPIView.as_view(), name="list"),
    path('search/', UserSearchAPIView.as_view(), name="search"),
]
