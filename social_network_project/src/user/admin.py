from django.contrib import admin
from user.models import User, Comments
# Register your models here.


class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = ['user_fio', 'firm_name', 'date_startwork', 'users_salary', 'users_experience']
    inlines = [ArticleInline]
    list_filter = ['date_startwork']

admin.site.register(User, ArticleAdmin)


