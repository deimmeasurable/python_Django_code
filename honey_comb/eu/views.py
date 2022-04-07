from django.http import HttpResponse
from django.shortcuts import render


def eu_register(request):
    return render(request, "register.html", context={"country": "European"})


def eu_login(request):
    return render(request, "login.html", context={"country": "European"})
# Create your views here.
