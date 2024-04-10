from django.contrib import admin
from django.urls import path, include
from apps.warehouses import views

urlpatterns = [
    path('create/', views.CreateWarehouseAPI.as_view(), name="create"),
    path('my/', views.MyWarehouseListAPI.as_view(), name="my"),
    path('list/', views.WarehouseListAPI.as_view(), name="list"),
    path('status/list/', views.ListStatusAPI.as_view(), name="status-list"),
    path('status-payment/list/', views.ListStatusPaymentAPI.as_view(), name="status-payment-list"),
]