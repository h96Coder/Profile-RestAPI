from django.contrib import admin
from .models import UserProfile,ProfileFeedItem
admin.site.register(UserProfile)
admin.site.register(ProfileFeedItem)


# class ProfileFeedItemAdmin(admin.ModelAdmin):
#     list_display = ("id", 'user_profile', 'status_text')
# admin.site.register(ProfileFeedItem, ProfileFeedItemAdmin)

# Register your models here.
