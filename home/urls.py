from django.urls import path
from . import views

app_name='home'

urlpatterns = [
    path('', views.index , name = 'home'),
    path('postAns/<int:queId>', views.postAns, name='postAns'),
    path('askQues/', views.askQues, name='askQues'),
    path('like/', views.like_answer ,name="like-asnwer"),
]
