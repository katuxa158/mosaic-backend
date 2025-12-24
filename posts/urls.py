from django.urls import path

from .views import PostListView, PostDetailView, PostCreateView

urlpatterns = [
    path('', PostListView.as_view()),
    path('<int:pk>/', PostDetailView.as_view()),
    path('', PostCreateView.as_view()),
]
