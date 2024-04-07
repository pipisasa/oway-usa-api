from django.urls import path, include
from apps.statics import views

admin_panel_urls = [
    path('users/', views.StaticsUserAPI.as_view(), name='statics_users'),
    path('warehouse-weight/', views.StaticsWarehouseWeightAPI.as_view(), name='warehouse_weight'),
]

urlpatterns = [
    path('admin_panel/', include(admin_panel_urls)),
]
