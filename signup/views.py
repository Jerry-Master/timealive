from django.http import HttpResponse, HttpResponseRedirect
from django import template
from django.contrib.auth.models import User
from django.urls import reverse
from django.shortcuts import render
from .forms import SignupForm
from schedule.models import Physician


def index(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, password=password)
            user.save()
            physician = Physician.objects.create(user=user, name='JPC')
            physician.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            print('error')
            print(form.errors)
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignupForm()
    return render(request, 'registration/signup.html', {'form': form})