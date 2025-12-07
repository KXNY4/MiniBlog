from django import forms
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Posts


class PostsCreateForm(forms.ModelForm):
    title = forms.CharField(max_length=200, min_length=3, required=True, widget=forms.TextInput(attrs={'placeholder': _('Заголовок')}))
    is_active = forms.BooleanField(required=False)
    class Meta:
        model = Posts
        fields = ['title', 'body', 'is_active']