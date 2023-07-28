from django.shortcuts import render,HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User

# Create your views here.

def register(request):

    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if (password1 == password2):
                if (not User.objects.filter(username=uname).exists()):
                    if (not User.objects.filter(email=email).exists()):
                        user = User.objects.create_user(username=uname, password=password1, email=email)
                        user.save()
                        messages.success(request,'You Are Registered Successfully!')
                        return redirect('/users/login')
                    else:
                        messages.info(request, 'Email Already registered')
                        return render(request, 'register.html')
                else:
                    messages.info(request, 'Username Already Exist')
                    return render(request, 'register.html')
            else:
                messages.info(request, 'Password Mismatch')
                return render(request, 'register.html')
        else:
            return render(request, 'register.html')
    except:
        pass 



def loginCustomer(request):
    try:
        if request.method=="POST":
            username = request.POST['Username']
            Pass = request.POST.get('Password')
            user = authenticate(username=username, password=Pass)
            if user is not None:
                login(request, user)
                messages.info(request,f"Welcome {username}! ")
                return redirect("/")

            else:
                messages.error(request,"Invalid username or password.")
                return render(request,'login.html')

        return render(request,'login.html')
    except:
        pass


def logoutCustomer(request):
    try:
        if request.user.is_anonymous:
            return redirect("/users/login")
        else:
            logout(request)
            messages.success(request,"Logged Out Successfully!")
        return redirect("/users/login")
    except:
        pass
