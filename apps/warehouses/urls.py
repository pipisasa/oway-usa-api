from django.contrib import admin
from django.urls import path, include
from apps.warehouses import views

urlpatterns = [
    path('create/', views.CreateWarehouseAPI.as_view(), name="create"),
    path('get/<int:id>/', views.WarehouseGetAPI.as_view(), name="get"),
    path('product/create/', views.CreateWarehouseProductAPI.as_view(), name="create-product"),
    path('product/list/', views.WarehouseProductListAPI.as_view(), name="list-product"),
    path('product/delete/', views.DeleteWarehouseProductAPI.as_view(), name="delete-product"),
    path('product/update/<int:pk>/', views.UpdateWarehouseProductAPI.as_view(), name="update-product"),
    path('my/', views.MyWarehouseListAPI.as_view(), name="my"),
    path('list/', views.WarehouseListAPI.as_view(), name="list"),
    path('product/get/<str:track_number>/', views.WarehouseProductGetAPI.as_view(), name="get-product"),
    path('update/<int:pk>/', views.UpdateWarehouseAPI.as_view(), name="update"),
    path('product/update/', views.UpdatesWarehouseProductAPI.as_view(), name="update"),
    path('delete/<int:id>/', views.DeleteWarehouseAPI.as_view(), name="update"),
    path('status/list/', views.ListStatusAPI.as_view(), name="status-list"),
    path('status-payment/list/', views.ListStatusPaymentAPI.as_view(), name="status-payment-list"),
]