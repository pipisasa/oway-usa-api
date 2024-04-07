from django.urls import path, include
from apps.statics import views

admin_panel_urls = [
    path('users/', views.StaticsUserAPI.as_view(), name='statics_users'),
    path('warehouse-weight/', views.StaticsWarehouseWeightAPI.as_view(), name='warehouse_weight'),
    path('warehouse-delivered/', views.StaticsWarehouseDeliveredAPI.as_view(), name='warehouse_delivered'),
    path('warehouse-paid/', views.StaticsWarehousePaidAPI.as_view(), name='warehouse_paid'),
]

urlpatterns = [
    path('admin_panel/', include(admin_panel_urls)),
]
