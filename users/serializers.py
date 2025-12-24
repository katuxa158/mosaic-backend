from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Role

User = get_user_model()

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'full_name',
            'posts_count',
            'is_online',
            'last_login',
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'full_name', 'avatar', 'posts_count', 'is_online')


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'full_name', 'password')

    def create(self, validated_data):
        role = Role.objects.get(name='User')
        return User.objects.create_user(
            username=validated_data['username'],
            full_name=validated_data['full_name'],
            password=validated_data['password'],
            role=role
        )
