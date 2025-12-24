from django.db import transaction

from posts.models import Post
from reactions.models import Reaction


class ReactionService:

    @staticmethod
    @transaction.atomic
    def set_reaction(*, user, post: Post, reaction_type: str):
        reaction, created = Reaction.objects.select_for_update().get_or_create(
            user=user,
            post=post,
            defaults={'type': reaction_type}
        )

        if created:
            ReactionService._increment(post, reaction_type)
            return

        if reaction.type == reaction_type:
            return

        ReactionService._decrement(post, reaction.type)
        reaction.type = reaction_type
        reaction.save(update_fields=['type'])
        ReactionService._increment(post, reaction_type)

    @staticmethod
    def _increment(post: Post, reaction_type: str):
        if reaction_type == Reaction.LIKE:
            post.likes_count += 1
        else:
            post.dislikes_count += 1
        post.save(update_fields=['likes_count', 'dislikes_count'])

    @staticmethod
    def _decrement(post: Post, reaction_type: str):
        if reaction_type == Reaction.LIKE:
            post.likes_count -= 1
        else:
            post.dislikes_count -= 1
        post.save(update_fields=['likes_count', 'dislikes_count'])