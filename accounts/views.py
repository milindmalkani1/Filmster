from django.shortcuts import render, redirect
from accounts.forms import RegisterationForm
from django.views.generic import CreateView, FormView
from accounts.models import MyUser
from django.urls import reverse

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegisterationForm()

    args = {'form': form}
    return render(request, 'accounts/register_form.html', args)

def profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html', args)
