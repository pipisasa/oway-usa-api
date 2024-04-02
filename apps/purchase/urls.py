from django.urls import path

from apps.purchase import views

urlpatterns = [
    path('add/', views.CreatePurchase.as_view(), name='add'),
    path('list/', views.PurchaseList.as_view(), name='list'),
    path('update/<int:pk>/', views.PurchaseUpdate.as_view(), name='update'),
]
