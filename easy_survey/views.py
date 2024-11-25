from django.http import HttpResponseRedirect
from django.urls import reverse
from user_auth.forms import UserForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from create_form.models import Form

@login_required
def login_root_redirect(request):
    return redirect('/easy_survey/')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect("/easy_survey/")
    else:
        form = UserForm
    return render(request, 'easy_survey/register.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'easy_survey/user_list.html', {'users':users})

def logout_view(request):
    #Logout the user
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    forms = Form.objects.filter(creator = request.user)
    return render(request, "easy_survey/index.html", {
        "forms": forms
    })

def results(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    forms = Form.objects.filter(creator = request.user)
    return render(request, "easy_survey/results.html", {
        "forms": forms
    })