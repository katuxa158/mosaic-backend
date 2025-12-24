from django.urls import path
from .views import (
    RegisterView,
    LogoutView,
    MeView,
    UserSearchView,
    AdminUsersView,
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('me/', MeView.as_view()),
    path('search/', UserSearchView.as_view()),
    path('admin/', AdminUsersView.as_view()),
]