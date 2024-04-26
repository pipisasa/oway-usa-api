from django.urls import path

from apps.clients_outside_of_illinois import views

urlpatterns = [
    path("add/", views.AddClient.as_view(), name="add_client"),
    path("list/", views.ClientsOutsideOfIllinoisListView.as_view(), name="list"),
    path("update_delete/<int:pk>/", views.ClientRetrieveUpdateDestroyAPIView.as_view(),
         name="update_delete"),
]
