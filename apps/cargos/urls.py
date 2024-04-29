from django.urls import path
from apps.cargos import views

urlpatterns = [
    path('create/', views.CargoCreateAPI.as_view(), name='cargo_create'),
    path('list/', views.CargoListAPI.as_view(), name='cargo_list'),
    path('update/<int:id>/', views.CargoUpdateAPI.as_view(), name='cargo_update'),
    path('delete/<int:id>/', views.CargoDeleteAPI.as_view(), name='cargo_delete'),
    path('get/<int:id>/', views.CargoGetAPI.as_view(), name='cargo_detail'),
]
