from django.contrib import admin

from .models import *


class UserAdmin(admin.ModelAdmin):
    list_display = [field.name for field in User._meta.fields]

    class Meta:
        model = User

admin.site.register(User, UserAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in StatusOfUser._meta.fields]

    class Meta:
        model = StatusOfUser

admin.site.register(StatusOfUser, StatusAdmin)


class UserImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserImage._meta.fields]

    class Meta:
        model = UserImage

admin.site.register(UserImage, UserImageAdmin)