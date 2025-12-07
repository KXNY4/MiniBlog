from django.shortcuts import redirect
from django.views import View

from Posts.models import Posts
from PostsLike.models import PostLikes


class ToggleLikeView(View):
    def post(self, request, *args, **kwargs):
        post = Posts.objects.get(slug=kwargs['post_slug'])
        like, created = PostLikes.objects.get_or_create(user=request.user, post=post)
        if not created:
            like.delete()
        return redirect(post.get_absolute_url())