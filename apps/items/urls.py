from django.urls import path
from apps.items import views

urlpatterns = [
    path('create/', views.CreateItemAPI.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateItemAPI.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteItemAPI.as_view(), name='delete'),
    path('get/<int:id>/', views.ItemDetailAPI.as_view(), name='detail'),
    path('list/', views.ItemListAPI.as_view(), name='list'),
    path('category/create/', views.CreateCategoryAPI.as_view(), name='create'),
    path('category/update/<int:pk>/', views.UpdateCategoryAPI.as_view(), name='update'),
    path('category/delete/<int:id>/', views.DeleteCategoryAPI.as_view(), name='delete'),
    path('category/get/<int:id>/', views.CategoryDetailAPI.as_view(), name='detail'),
    path('category/list/', views.CategoryListAPI.as_view(), name='list'),
]