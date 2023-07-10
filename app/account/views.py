from django.contrib.auth import login, logout
from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, UserTokenSerializer, LoginSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects
    serializer_class = UserSerializer
    filterset_fields = ['username']
    search_fields = ['username']
    ordering_fields = ['created_at', 'id']
    ordering = ['id']


class ProfileAPIView(generics.RetrieveUpdateAPIView):
    queryset = User.objects
    serializer_class = UserSerializer

    def get_object(self):
        return self.get_queryset().get(username=self.request.user.username)


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        login(request, user)
        jwt_token = RefreshToken.for_user(user)
        user.token = {
            'refresh': str(jwt_token),
            'access': str(jwt_token.access_token),
        }
        return Response(UserTokenSerializer(user).data)


class LogoutAPIView(generics.GenericAPIView):
    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response(status=status.HTTP_204_NO_CONTENT)
