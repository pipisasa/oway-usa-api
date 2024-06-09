from django.contrib import admin
from django.urls import path, include
from apps.users import views

urlpatterns = [
    path('register/', views.SignUpAPIView.as_view(), name="register"),
    path('login/', views.SignInAPIView.as_view(), name="login"),
    path('auth/google/', views.GoogleLoginAPI.as_view(), name="login-google"),
    path('profile/', views.ProfileAPIView.as_view(), name="profile"),
    path('profile/<int:id>/', views.ProfileDetailAPI.as_view(), name="profile"),
    path('activation_account/', views.ActivationAccountAPIView.as_view(), name="activation_account"),
    path('change_password/', views.ChangePasswordView.as_view(), name="change_password"),
    path('forgot_pass_send_activation_code/',
         views.ForgotPasswordSendActivationCodeView.as_view(),
         name='forgot_pass_send_activation_code'),
    path('forgot_pass_complete/',
         views.ForgotPasswordCompleteView.as_view(),
         name='forgot_pass_complete'),
]
