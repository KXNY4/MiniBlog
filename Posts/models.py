from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from Posts.utils import translit_to_eng


USERMODEL = get_user_model()


class Posts(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False, verbose_name=_('Заголовок'))
    slug = models.SlugField(unique=True, blank=True, verbose_name='Slug')
    body = models.TextField(verbose_name=_('Содержимое'))
    author = models.ForeignKey(USERMODEL, on_delete=models.CASCADE, related_name='posts', verbose_name=_('Автор'))
    created_at = models.DateTimeField(auto_now_add=True, blank=True, verbose_name=_('Дата создания'))
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name=_('Последнее обновление'))
    is_active = models.BooleanField(blank=True, verbose_name=_('Статус'))
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(translit_to_eng(self.title))
            slug = base_slug
            counter = 1
            while Posts.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = _('Пост')
        verbose_name_plural = _('Посты')

    def __str__(self):
        return str(_(self.title))


    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"post_slug": self.slug})
    
    def get_slug_to_delete_post(self):
        return reverse("posts:delete", kwargs={"post_slug": self.slug})
    
    def get_slug_to_like_post(self):
        return reverse("posts:like", kwargs={"post_slug": self.slug})