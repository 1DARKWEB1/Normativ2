from django.contrib import admin
from .models import BotUser


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ("user_id", "username", "full_name", "created_at")
    search_fields = ("username", "full_name")
