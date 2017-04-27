from django.db import models
from user.models import User
from user.models import UserImage


class Relationship (models.Model):
    user = models.ForeignKey(User, blank=True, null=True, default=None)
    userFan = models.ForeignKey(UserImage, blank=True, null=True, default=None)

    def __str__(self):
        return "Подписчик %i %s %s %s" % (self.id, self.userFan.user.surname, self.userFan.user.name,
                                          self.userFan.image)
        # отображение в админке

    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'