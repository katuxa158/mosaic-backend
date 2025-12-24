from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from posts.models import Post
from reactions.models import Reaction
from reactions.services import ReactionService


class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        ReactionService.set_reaction(
            user=request.user,
            post=post,
            reaction_type=Reaction.LIKE
        )
        return Response({'detail': 'Liked'})


class DislikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        post = get_object_or_404(Post, id=post_id)
        ReactionService.set_reaction(
            user=request.user,
            post=post,
            reaction_type=Reaction.DISLIKE
        )
        return Response({'detail': 'Disliked'})