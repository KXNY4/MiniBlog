from django.contrib import admin
from django.contrib.auth import get_user_model


USERMODEL = get_user_model()

@admin.register(USERMODEL)
class AdminUsers(admin.ModelAdmin):
    ...