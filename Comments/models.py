from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from Posts.models import Posts


USERMODEL = get_user_model()


class Comments(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Пост'))
    author = models.ForeignKey(USERMODEL, on_delete=models.CASCADE, related_name='comments', verbose_name=_('Автор'))
    body = models.TextField(verbose_name=_('Содержимое'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(_(f"Комментарий от '{self.author}' на '{self.post}'"))
    
    class Meta:
        verbose_name = _('Комментарий')
        verbose_name_plural = _('Комментарии')
        ordering = ['-created_at']