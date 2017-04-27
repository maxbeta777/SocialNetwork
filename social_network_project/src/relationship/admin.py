from django.contrib import admin
from .models import *


class RelationshipAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Relationship._meta.fields]

    class Meta:
        model = Relationship

admin.site.register(Relationship, RelationshipAdmin)
