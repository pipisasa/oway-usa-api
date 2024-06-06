from django.urls import path

from apps.logos import views

urlpatterns = [
    path('add/', views.LogoAddView.as_view(), name='logo_add'),
    path('list/', views.LogoListView.as_view(), name='logo_list'),
    path('update_delete/<int:pk>/', views.LogoRetrieveUpdateDestroyAPIView.as_view(),
         name='logo_update_delete'),
]
