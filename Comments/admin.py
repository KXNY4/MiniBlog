from django.contrib import admin

from Comments.models import Comments


@admin.register(Comments)
class AdminComments(admin.ModelAdmin):
    list_display = ('post', 'author', 'body', 'created_at')
    readonly_fields = ('created_at', )