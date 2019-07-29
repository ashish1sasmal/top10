from django.shortcuts import render
from .models import Album
# Create your views here.
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required



def index(request):
	album=Album.objects.all()
	return render(request,'top10/index.html',{'album':album})

@login_required
def user_logout(request):
	logout(request)
	print("Logged Out!")
	return HttpResponseRedirect(reverse('index'))

def user_login(request):
	if request.method=='POST':
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(username=username,password=password)

		if user:
			if user.is_active:
				login(request,user)
				return HttpResponseRedirect(reverse('index'))
			else:
				return HttpResponse("Account Not Active!!")

		else:
			return HttpResponse("Invalid logins details supplied!")

	else:
		return render(request,'top10/login.html',{})


def register(request):
	registered=False
	if request.method=='POST':
			user_form=UserForm(data=request.POST)
			profile_form=UserInfoForm(data=request.POST)
			if user_form.is_valid() and profile_form.is_valid():
				user=user_form.save()
				user.set_password(user.password)
				profile=profile_form.save(commit=False)
				profile.user=user

				if 'picture' in request.FILES:
					profile.picture=request.FILES['picture']

				profile.save()
				registered=True

			else:
				print(user_form.errors,profile_form.errors)

	else:
		user_form=UserForm()
		profile_form=UserInfoForm()
	return render(request,'top10/registeration.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})




