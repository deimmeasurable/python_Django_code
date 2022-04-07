from django.contrib import admin
from django.http import HttpResponse
from django.urls import path

from ng.views import ng_register, ng_login

urlpatterns = [

    path('register/', ng_register),
    path('login/', ng_login),

]
