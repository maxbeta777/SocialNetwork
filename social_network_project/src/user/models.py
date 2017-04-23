from django.db import models

# Create your models here.
class User(models.Model):
    class Meta():
        db_table = 'user'
    user_fio = models.CharField(max_length=200)
    firm_name = models.CharField(max_length=200)
    date_startwork = models.DateTimeField()
    user_likes = models.IntegerField(default=0)
    users_salary = models.IntegerField(default=0)
    users_experience = models.IntegerField(default=0)
    #users_pr = models.IntegerField(default=0)



class Comments(models.Model):
    class Meta():
        db_table = 'comments'
    comments_text = models.TextField(verbose_name="Otz")
    comments_art = models.ForeignKey(User)