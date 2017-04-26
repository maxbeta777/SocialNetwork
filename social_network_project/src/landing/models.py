from django.db import models


class Guest(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=128)

    def __str__(self):
        return "Гость %i %s %s" % (self.id, self.name, self.email,)  # отображение в админке

    class Meta:
        verbose_name = 'Guest'
        verbose_name_plural = 'Guests'