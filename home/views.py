from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .forms import questions, answers
from datetime import datetime
from home.models import Question, Answer, Like
from django.contrib import messages

# Create your views here.
def index(request):
    que_set = Question.objects.all()
    name = request.user
    data={"ques":que_set, "name":name}
    try:
        return render(request, 'index.html',data)
    
    except:
        pass


def postAns(request, queId):
    a=answers()
    query_set = Question.objects.get(qid=queId)
    data={"aForm":a, 'ques':query_set}
    try:
        if request.method == 'POST': 
            if request.user.is_authenticated:
                ans = request.POST.get('answer')
                uname = request.user.username
                answer = Answer(ans=ans, queid=query_set, like=0, uname=uname, date=datetime.today())
                answer.save()
                messages.success(request, "Answer Posted Successfully!")
                return redirect("/")
            else:
                messages.warning(request, "You are not Logged in")

        return render(request, 'postAns.html',data)
    except Exception as e:
        print(e)
        


def askQues(request):
    q=questions()
    query_set = Question.objects.all()
    query_set= reversed(query_set)
    data={"qForm":q, 'ques':query_set}
    try:
        if request.method == 'POST':
            form = questions(request.POST)
            if form.is_valid():
                que = request.POST['question']
                uname = request.user.username
                question = Question(uname=uname, que=que, date=datetime.today())
                question.save()
                messages.success(request, "Question Submitted Successfully!")
            return HttpResponseRedirect('/askQues', data)

        return render(request, 'askQues.html',data)
    except:
        pass


def like_answer(request):
    uname = request.user
    if request.method == "POST":
        answer_id = request.POST.get('answer_id')
        answer_obj = Answer.objects.get(aid=answer_id)
        
        if uname in answer_obj.liked.all():
            answer_obj.liked.remove(uname)
        else:
            answer_obj.liked.add(uname)

        like, created = Like.objects.get_or_create(uname=uname, answer_id=answer_id)
        if not created:
            if like.value =='Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()
    return redirect('/')
