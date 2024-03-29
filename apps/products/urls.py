from django.urls import path
from apps.products import views

urlpatterns = [
    path('add/', views.ProductsCreateAPIView.as_view(), name="products-add"),
    path('list/', views.ProductsListAPIView.as_view(), name="products-list"),
    path('delete_update/<int:pk>/', views.ProductsDetailAPIView.as_view(), name="products-detail"),
]
