from django.urls import path


# def register(request):
#     return HttpResponse("filling this form!")
from honey_comb.eu.views import eu_register, eu_login

urlpatterns = [
    path('register/', eu_register),
    path('login/', eu_login),
]
