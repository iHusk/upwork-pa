from django.contrib import admin

from .models import UserProfile


class UserProfileList(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'email_notification_active')
    list_filter = ('email', 'first_name')
    search_fields = ['email']


admin.site.register(UserProfile, UserProfileList)
