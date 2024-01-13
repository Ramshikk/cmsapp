
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('adminold/', admin.site.urls),
    path('changepassword',views.changepwd,name='pwd'),
    path('Login',views.adminlogin),
    
    
]
