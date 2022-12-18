# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import render


def SignUpView(request):
    return render(request, 'registeration/login.html')
