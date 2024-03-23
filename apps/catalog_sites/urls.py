from django.urls import path

from apps.catalog_sites import views

urlpatterns = [
    path('create/', views.CreateCatalogSiteAPI.as_view(), name="create"),
    path('list/', views.ListCatalogSitesAPI.as_view(), name="list"),
    path('delete/<int:id>/', views.DeleteCatalogSitesAPI.as_view(), name="delete"),
    path('update/<int:id>/', views.UpdateCatalogSiteAPI.as_view(), name="update"),
]
