from django.shortcuts import render
from .models import *
from django.http import *


def home(request):
	obj = student2.objects.all()
	return render(request, 'index.html', {'obj':obj})


def page(request):
	obj = student2.objects.all()
	return render(request, 'main.html', {'obj':obj})
# Create your views here.


def first(request):
	obj = student2.objects.all()
	return render(request, 'first.html', {'obj':obj})



def login(request):
	obj = student2.objects.all()
	return render(request, 'login.html', {'obj':obj})



def register(request):
	obj = student2.objects.all()
	return render(request, 'register.html', {'obj':obj})