from django.http import HttpResponse
from django.shortcuts import render


def ng_register(request):
    return render(request, "register.html", context={"country": "Nigeria"})


def ng_login(request):
    return render(request, "login.html", context={"country": "Nigeria"})
# Create your views here.
