from django.urls import path
from apps.address import views

urlpatterns = [
    path('create/', views.CreateAddressAPI.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateAddressAPI.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteAddressAPI.as_view(), name='delete'),
    path('get/<int:id>/', views.AddressDetailAPI.as_view(), name='detail'),
    path('list/', views.AddressListAPI.as_view(), name='list'),
]