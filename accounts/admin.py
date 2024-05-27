from django.contrib import admin
from .models import *

class UserDataAdmin(admin.ModelAdmin):
    list_display = ['user', 'VK', 'Instagram', 'Telegram', 'AboutMe']
    list_editable = ['VK', 'Instagram', 'Telegram', 'AboutMe']
    list_display_links = ['user']
    class Meta:
        model = UserData

admin.site.register(UserData, UserDataAdmin)