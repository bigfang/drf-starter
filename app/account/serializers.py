from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User, UserToken


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class UserTokenSerializer(serializers.ModelSerializer):
    access_token = serializers.CharField(max_length=255, read_only=True, source='token.access')
    refresh_token = serializers.CharField(max_length=255, read_only=True, source='token.refresh')

    class Meta:
        model = UserToken
        fields = ['id', 'username', 'access_token', 'refresh_token']


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)

    class Meta:
        fields = ['username', 'password']

    def validate(self, attrs) -> User:
        user = authenticate(username=attrs['username'], password=attrs['password'])
        assert isinstance(user, User | None)

        if not user:
            raise serializers.ValidationError('Incorrect username or password.')
        if (not user.is_active) or user.is_deleted:
            raise serializers.ValidationError('User is disabled.')

        return user
