from django.urls import path

from apps.cities import views

urlpatterns = [
    path('list/', views.ListCityAPI.as_view(), name="list"),
]