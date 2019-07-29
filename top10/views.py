from django.shortcuts import render
from .models import Album
# Create your views here.



def index(request):
	album=Album.objects.all()
	return render(request,'top10/index.html',{'album':album})