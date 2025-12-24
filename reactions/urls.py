from django.urls import path
from .views import LikePostView, DislikePostView

urlpatterns = [
    path('<int:post_id>/like/', LikePostView.as_view()),
    path('<int:post_id>/dislike/', DislikePostView.as_view()),
]