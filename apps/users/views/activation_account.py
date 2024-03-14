from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.serializers import ActivationAccountSerializer


class ActivationAccountAPIView(APIView):
    serializer_class = ActivationAccountSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.activate()
            return Response('Account successfully activated', status=200)