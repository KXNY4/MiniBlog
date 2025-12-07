from django import forms
from django.utils.translation import gettext_lazy as _

from Comments.models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        widgets = {
            'text': forms.Textarea(attrs={'rows': 3, 'placeholder': _('Оставьте комментарий...')})
        }