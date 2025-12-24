from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, RegisterSerializer, AdminUserSerializer
from .models import User
from .permissions import IsAdmin

class AdminUsersView(generics.ListAPIView):
    """
    Только для администратора.
    Возвращает список всех пользователей с их активностью.
    """
    queryset = User.objects.all().order_by('-last_login')
    serializer_class = AdminUserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]


class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'detail': 'User created'})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.user.is_online = False
        request.user.save(update_fields=['is_online'])
        return Response({'detail': 'Logged out'})


class MeView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        q = self.request.query_params.get('q', '')
        return User.objects.filter(username__icontains=q)