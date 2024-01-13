from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def changepwd(request):
    return render(request,'changepwd.html')
def adminlogin(request):
    return render(request,'index.html')

# Create your views here.
