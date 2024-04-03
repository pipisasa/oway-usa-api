from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView

from apps.add_user_in_ap.serialiers import AddUserSerializer
from apps.users.models import User, PassportFront, PassportBack
from apps.users.serializers import ProfileSerializer


class AddUserForAdminAPIView(APIView):
    serializer_class = AddUserSerializer
    permission_classes = [IsAdminUser]

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            user = User.objects.create(
                phone_number=data.get('phone_number'),
                email=data.get('email'),
                first_name=data.get('first_name', ''),
                last_name=data.get('last_name', ''),
                password=data.get('password'),
                is_active=True
            )
            user.save()
            front_image = PassportFront.objects.create(
                user=user,
                front_image=data.get('front_image')
            )
            front_image.save()
            back_image = PassportBack.objects.create(
                user=user,
                back_image=data.get('back_image')
            )
            back_image.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomPagination(PageNumberPagination):
    page_size = 7
    page_size_query_param = 'page_size'
    max_page_size = 100


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = CustomPagination
    permission_classes = [IsAdminUser]
