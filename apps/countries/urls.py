from django.urls import path

from apps.countries import views

urlpatterns = [
    path('list/', views.ListCountryAPI.as_view(), name="list"),
]
