from django.urls import path
from apps.contacts import views

urlpatterns = [
    path('create/', views.CreateContactAPI.as_view(), name='create'),
    path('update/<int:pk>/', views.UpdateContactAPI.as_view(), name='update'),
    path('delete/<int:id>/', views.DeleteContactAPI.as_view(), name='delete'),
    path('get/<int:id>/', views.ContactDetailAPI.as_view(), name='detail'),
    path('list/', views.ContactListAPI.as_view(), name='list')
]