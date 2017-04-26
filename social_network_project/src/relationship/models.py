from django.db import models
from user.models import User
from user.models import UserImage


class Relationship (models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    userImage = models.ForeignKey(UserImage, blank=True, null=True, default=None)

    def __str__(self):
        return "Подписчик %i %s %s %s" % (self.id, self.user.surname, self.user.name, self.userImage.image)
        # отображение в админке

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'