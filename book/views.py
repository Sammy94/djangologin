from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from .models import *
# Create your views here.

def index(request):
	return render(request,"book/signup.html")


def signup(request):
	user = User(username=request.POST.get('username') , first_name= request.POST.get('name'), last_name=request.POST.get('lname') , password=request.POST.get('password') )
	user.save()
	if user is not None:
		return HttpResponse("You have successfuuly logged in")
	else:
		return HttpResponse("Username already taken")


def login(request):
	if request.method == "GET":
		return render(request,'book/login.html')
	if request.method == "POST":
		user = authenticate(username= request.POST.get('username'), password=request.POST.get('password'))
		print(user)
		if user is not None:
			return render(request,"book/index.html")
		else:
			return HttpResponse("Authentication failed")


def homepage(request):
	product= products.objects.all()
	print(products.objects.get(price=30))
	context={
	"products":product,
	}
	return render(request,"book/index.html",context)
    # Do something for authenticated users.
	
def logout_view(request):
	logout(request)
	return render(request,'book/login.html')


 





