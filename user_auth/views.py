from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import UserForm
from .models import Profile
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver

@login_required
def login_root_redirect(request):
    return redirect('/')


def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the User object
            # Extract the role and save it in the Profile model
            # If the form is valid, the cleaned and validated data is stored in form.
            role = form.cleaned_data.get('role')
            Profile.objects.create(user=user, role=role)
            
            # Log the user in
            login(request, user)
            return redirect("/")
    else:
        form = UserForm()
    return render(request, 'easy_survey/register.html', {'form': form})

    
# def register(request):
#     if request.method == 'POST':
#         form = UserForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             login(request, user)
#             return redirect("/")
#     else:
#         form = UserForm
#     return render(request, 'easy_survey/register.html', {'form': form})

@login_required
def user_list(request):
    users = User.objects.all()
    return render(request, 'easy_survey/user_list.html', {'users':users})

def logout_view(request):
    #Logout the user
    logout(request)
    return HttpResponseRedirect(reverse('index'))


# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()


