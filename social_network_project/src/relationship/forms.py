from django import forms
from .models import *


class RelationshipForm(forms.ModelForm):

    class Meta:
        model = Relationship
        exclude = [""]

