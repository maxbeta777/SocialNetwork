from django.forms import ModelForm
from user.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
        #exclude = ['comments_article']
