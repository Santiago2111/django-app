from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from .forms import UserForm

# Create your views here.
def index(request):
    return HttpResponse("::: WELCOME TO MY SITE :::")

def list_users(request):
    #return HttpResponse("Here you find a list of users")
    users = User.objects.all()
    return render(request, 'academics/list_user.html', {'users': users})

def create_user(request):
    if request.method == ' POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = UserForm()
    return render(request, 'academics/create_user.html', {'form': form})