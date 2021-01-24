from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password  # password 암호화 
from .models import Fcuser
from .forms import LoginForm


# Create your views here.
def home(request):
    user_id = request.session.get('user')

    if user_id:
        fcuser = Fcuser.objects.get(pk=user_id)
        return HttpResponse(fcuser.username)
    return render(request, 'fcuser/home.html')


def register(request):
    if request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # re_password = request.POST['re-password']
        
        username = request.POST.get('username', None)
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        error = ''
        if not (username and useremail and password and re_password ):
            error = 'Please enter all blanks!'
            return render(request, 'fcuser/register.html', {'error': error})

        elif password != re_password:
            # return HttpResponse('Passwords do not match!')  # 별도의 html 페이지로 이동힘
            error = 'Passwords do not match!'
            return render(request, 'fcuser/register.html', {'error': error})

        else:
            fcuser = Fcuser(
                username=username,
                useremail=useremail,
                password=make_password(password)
            )
            fcuser.save()
            return redirect('register')
    else:
        return render(request, 'fcuser/register.html')


def login(request):
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():  # error 가 발생했다고 판단되면 forms 안에 error 정보까지 들어있다
            # session
            request.session['user'] = forms.user_id
            return redirect('/')
    else:  
        forms = LoginForm()
    return render(request, 'fcuser/login.html', {'forms': forms})
"""
def login(request):  # Using Session
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        
        error = ''
        if not (username and password):
            error = 'Please enter all blanks!'
            return render(request, 'fcuser/login.html', {'error': error})
        else:
            fcuser = Fcuser.objects.get(username=username)
            if check_password(password, fcuser.password):
                request.session['user'] = fcuser.id
                return redirect('/')  # /: root if this site
                # login
            else:
                error = 'Your Password is wrong'
                return render(request, 'fcuser/login.html', {'error': error})

    else:
        return render(request, 'fcuser/login.html')
"""


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')
        