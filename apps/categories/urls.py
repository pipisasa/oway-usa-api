from django.urls import path

from apps.categories import views

urlpatterns = [
    path('create/', views.CreateCategoryAPI.as_view(), name="create"),
    path('list/', views.ListCategoryAPI.as_view(), name="list"),
    path('delete/<int:id>/', views.DeleteCategoryAPI.as_view(), name="delete"),
    path('update/<int:id>/', views.UpdateCategoryAPI.as_view(), name="update"),
]
