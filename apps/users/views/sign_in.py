from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers import SignInSerializer


class SignInAPIView(TokenObtainPairView):
    serializer_class = SignInSerializer