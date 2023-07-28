from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Question(models.Model):
    qid = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=50)
    que = models.CharField(max_length=200)
    date = models.DateField()
    
    def __str__(self):
        return self.que


class Answer(models.Model):
    aid = models.AutoField(primary_key=True, default=False)
    queid = models.ForeignKey(Question, related_name="answr", on_delete=models.CASCADE)
    uname = models.CharField(max_length=50)
    ans = models.TextField()
    liked = models.ManyToManyField(User, related_name="liked", default=None, blank=True)
    date = models.DateField()


#Using 'property' decorator to 'count_likes()' method
    @property
    def count_likes(self):
        return self.liked.all().count()
    
    def __str__(self):
        return self.ans

LIKE_CHOICES = (('Like','Like'),('Unlike','Unlike'))

class Like(models.Model):
    uname = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, default='Like',max_length=10)

    def __str__(self):
        return str(self.answer)