from datetime import datetime
from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Qualification(models.Model):
    qname=models.CharField(max_length=200)
    status=models.IntegerField(default=1)
    #class designation
class Designation(models.Model):
    designation=models.CharField(max_length=200)
    code=models.CharField(max_length=200)
    status=models.IntegerField(default=1)

#class for adding, editting and listing   class
class Addclass(models.Model):
    classs=models.CharField(max_length=200)
    status=models.IntegerField(default=1)


class Category(models.Model):
    categoryname=models.CharField(max_length=200)
class prodcuctcategory(models.Model):
    catid = models.ForeignKey('Category', on_delete=models.CASCADE)
    productname=models.CharField(max_length=200)

class Employee(models.Model):
    Ename=models.CharField(max_length=200)
    gender=models.IntegerField()
    dob=models.DateField()
    address=models.CharField(max_length=300)
    email=models.CharField(max_length=200)
    mobile=models.CharField(max_length=100)
    datejoing=models.DateField()
    Eimage=models.ImageField(upload_to='employees',null=True)
    qualid=models.ForeignKey('Qualification', on_delete=models.CASCADE)
    desid=models.ForeignKey('Designation', on_delete=models.CASCADE)
    salary=models.IntegerField()
    salaryday=models.CharField(max_length=100)
    status=models.IntegerField(default=1)
    




    