from django.contrib import admin
from django.urls import path, include
from apps.users import views

urlpatterns = [
    path('register/', views.SignUpAPIView.as_view(), name="register"),
    path('login/', views.SignInAPIView.as_view(), name="login"),
    path('profile/', views.ProfileAPIView.as_view(), name="profile"),
    path('activation_account/', views.ActivationAccountAPIView.as_view(), name="activation_account"),
]