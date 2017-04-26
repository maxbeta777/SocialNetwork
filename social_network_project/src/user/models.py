from django.db import models


class StatusOfUser(models.Model):

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = 'Status'

    description = models.CharField(max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.name


class User(models.Model):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    surname = models.CharField(max_length=200, blank=True, null=True, default=None)
    phone = models.CharField(max_length=48, blank=True, null=True, default=None)
    email = models.EmailField(blank=True, null=True, default=None)
    country = models.CharField(max_length=200, blank=True, null=True, default=None)
    city = models.CharField(max_length=200, blank=True, null=True, default=None)
    status = models.ForeignKey(StatusOfUser)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return "Пользователь %s %s" % (self.id,  self.status.description)


class UserImage(models.Model):

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'

    user = models.ForeignKey(User, blank=True, null=True, default=None)
    image = models.ImageField(upload_to='users_images/')
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " %s" % self.id


