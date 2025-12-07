from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from Posts.models import Posts


USERMODEL = get_user_model()


class PostLikes(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='liked_posts', verbose_name=_('Понравившийся пост'))
    user = models.ForeignKey(USERMODEL, on_delete=models.CASCADE, related_name='lakeds', verbose_name=_('Понравилось'))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Понравилось в'))

    class Meta:
        verbose_name = _('Лайк')
        verbose_name_plural = _('Лайки')
        ordering = ['-created_at']
        unique_together = ('post', 'user')

    def __str__(self):
        return str(_(f"{self.user} лайкнул {self.post}"))