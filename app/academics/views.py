from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("::: WELCOME TO MY SITE jorginho :::")

def list_persons(request):
    return HttpResponse(":::  :::")