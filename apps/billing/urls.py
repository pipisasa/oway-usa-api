from django.urls import path
from apps.billing import views

urlpatterns = [
    path('add/', views.BillingCreateAPIView.as_view(), name='billing_add'),
    path('update/<int:pk>/', views.UpdateBillingAPIView.as_view(), name='billing_update'),
    path('delete/<int:pk>/', views.DeleteBillingAPIView.as_view(), name='billing_delete'),
    path('my_billings/', views.MyBillingsAPIView.as_view(), name='my_billings')
]
