from django.db import models


class Recipe(models.Model):
    class Meta:
        verbose_name = 'Recipe'
        verbose_name_plural = 'Recipes'

    name = models.CharField(max_length=200, blank=True, null=True, default=None)
    calorie = models.IntegerField(default=0)
    ingredients = models.TextField(blank=True, null=True, default=None)
    recipe = models.TextField(blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id, self.name)