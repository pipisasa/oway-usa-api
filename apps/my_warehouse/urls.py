from django.urls import path
from apps.my_warehouse import views

urlpatterns = [
    path('add/', views.MyWarehouseAddView.as_view(), name='add'),
    path('update/<int:pk>/', views.MyWarehouseUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.MyWarehouseDelete.as_view(), name='delete'),
    path('list/', views.MyWarehouseListView.as_view(), name='list'),
]
