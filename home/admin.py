from django.contrib import admin
from home.models import Question, Answer, Like
# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('qid','uname','que')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('aid', 'queid', 'uname', 'ans')

class LikeAdmin(admin.ModelAdmin):
    list_display = ( 'value', 'uname', 'answer')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(Like, LikeAdmin)
