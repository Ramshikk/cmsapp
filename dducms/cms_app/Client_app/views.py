from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def frontpage(request):
    return render(request,'frontpage.html')
# Create your views here.
