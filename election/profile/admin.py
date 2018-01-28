from django.contrib import admin
from election.profile.models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email','name','is_active','is_superuser','created_at')

admin.site.register(UserProfile,UserProfileAdmin)