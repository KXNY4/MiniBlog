from django.contrib import admin

from Posts.models import Posts


@admin.register(Posts)
class AdminPosts(admin.ModelAdmin):
    list_display = ('title', 'author', 'updated_at', 'created_at')
    readonly_fields = ('created_at', 'updated_at')