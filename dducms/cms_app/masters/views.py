from asyncio.windows_events import NULL
import re
from tkinter import Variable
from unicodedata import category
from unittest import result
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User,auth
from django.contrib.auth import logout
from django.contrib.auth import get_user_model

from masters.models import Addclass, Designation, Qualification,Category, prodcuctcategory,Employee

# Edit qualification
def editqualification(request,itemid):
    if request.POST:
        details=Qualification.objects.get(id=itemid)
        details.qname=request.POST['fname']
        details.status=int(request.POST["statuss"]) 
        
        details.save()
        return redirect("quallist")

    details=Qualification.objects.get(id=itemid)
    result={
        'details':details,
    }
    return render(request,'EditQualification.html',result)
    


#view qualification
def qualificationlist(request):
    Details=Qualification.objects.all().values()
    listdt=loader.get_template("QualificationList.html")
    result={
        'Details':Details,
        
    }
    return HttpResponse(listdt.render(result,request))

def qualdelete(request,itmid):
    
    details=Qualification.objects.get(id=itmid)
    details.delete()
    return redirect("quallist")


@csrf_exempt
@login_required
def addqualification(request):
    if request.POST:
        message=""
        icon=0
        a=request.POST['fname']
        if Qualification.objects.filter(qname=a).exists():
            icon="warning"
            message="Qualification Already Exist"
            return render(request,'Qualification.html',{'message':message,'icon':icon})
        else:

                addqual=Qualification(qname=a)
                addqual.save()
                icon="success"
                message="Successfully added"
        
                return render(request,'Qualification.html',{'message':message,'icon':icon})
    else:
        return render(request,'Qualification.html')
    #adqual=loader.get_template("Qualification.html")
    #return HttpResponse(adqual.render())
@csrf_exempt 
def adddesignation(request):
    if request.POST:
        desig=request.POST["fname"]
        codes=request.POST["code"]
        icon=0
        if Designation.objects.filter(designation=desig).exists() and Designation.objects.filter(code=codes).exists() :
            icon="warning"
            su="Already Exist"     
            return render(request,'Designation.html',{'message':su,'icon':icon})
        else:
            adddes=Designation(designation=desig,code=codes)
            adddes.save()
            icon="success"
            su="Added Successfully"
            return render(request,'Designation.html',{'message':su, 'icon':icon})
    else:
        return render(request,'Designation.html')
    
def designationlist(request):
    details=Designation.objects.all().values()
    return render(request,'designationList.html',{'details':details})

#designation editting
def designationEdit(request,itemid):
    if request.POST:
        a=request.POST["desname"]
        b=request.POST["code"]
        c=int(request.POST["statuss"])
        details=Designation.objects.get(id=itemid)
        details.designation=a
        details.code=b
        details.status=c
        details.save()
        return redirect('deslist')

    details=Designation.objects.get(id=itemid) 
    return render(request,'DesignationEdit.html',{'details':details})


#delete designation from list
def designationDel(request,itemid):
    details=Designation.objects.get(id=itemid)
    details.delete()
    return redirect('deslist')
# add class details
@csrf_exempt
def classadd(request):
    if request.POST:
        ms=""
        icon=0
        a=request.POST['classname']
        if Addclass.objects.filter(classs=a).exists():
            icon="warning"
            return render(request,'classAdd.html',{'message':ms,'icon':icon})
        else:
            details=Addclass(classs=a)
            details.save()
            ms="success"
            return render(request,'classAdd.html',{'message':ms,'icon':icon})
        
#listitem=Addclass.objects.all().values()

    return render(request,'classAdd.html')


    
def division(request):
    return render(request,'Division.html')
def qualad(request):
    fname = request.POST.get('fname')
    return render(request,'qualificationadd.html',{'name':' welcome ........'},fname)
def studentreg(request):
    return render(request,'StudentRegistration.html')

def studentList(request):
    return render(request,'studentListing.html')
def studentedit(request):
    return render(request,'studentEdit.html')

def empreg(request):
    qualList=Qualification.objects.filter(status=1)
    desList=Designation.objects.filter(status=1)
    mismatch=""
    if request.POST:
        ename=request.POST['Ename']
        gender=request.POST["radio1"]
        dob=request.POST["dob"]
        address=request.POST["add"]
        email=request.POST["Email"]
        phone=request.POST["mobile"]
        doj=request.POST["doj"]
        qualid=int(request.POST['qual'])
        desid=int(request.POST["desig"])
        salary=request.POST["sal"]
        salday=request.POST["salday"]
        password=request.POST["pwd"]
        cpwd=request.POST["cpwd"]
        image=request.FILES['fileup']
       
        if password == cpwd:
             obj=Employee(Ename=ename,gender=gender,dob=dob,address=address,email=email,mobile=phone,datejoing=doj,salary=salary,salaryday=salday,desid_id=desid,qualid_id=qualid,Eimage=image)
             obj.save()
            
        
             userobj=User.objects.create_user(username=ename,password=password,first_name=ename,email=email)
             userobj.save()
        
             return render(request,'Registration.html',{'qualist':qualList,'deslist':desList,'mismatch':mismatch})
        else:
            mismatch="Password mismatch"
            return render(request,'Registration.html',{'qualist':qualList,'deslist':desList,'mismatch':mismatch})

    return render(request,'Registration.html',{'qualist':qualList,'deslist':desList,'mismatch':mismatch})

    #return render(request,'Registration.html')
# select employee whose corresponding designation
def emplist(request):
    #emplist=Employee.objects.all()
    emplist=Employee.objects.select_related('desid').all()
    return render(request,'RegistrationList.html',{'emplist':emplist})

def empdetailedview(request,empid):
    empdetail=Employee.objects.select_related('desid','qualid').all()
    return render(request,'RegistrationList.html',{'empdetail':empdetail})


def empedit(request,empid):
    qualList=Qualification.objects.filter(status=1)
    desList=Designation.objects.filter(status=1)
    emplist=Employee.objects.get(id=empid)
    if request.POST:
       
        emplist.Ename=request.POST['Ename'] 
        emplist.gender=request.POST["radio1"]
        emplist.dob=request.POST["dob"]
        emplist.address=request.POST["add"]
        emplist.email=request.POST["Email"]
        emplist.mobile=request.POST["mobile"]
        emplist.datejoing=request.POST["doj"]
        emplist.salary=request.POST["sal"]
        emplist.salaryday=request.POST["salday"]
        emplist.desid_id=int(request.POST["desig"])
        emplist.qualid_id=int(request.POST['qual'])
        emplist.save()
        return redirect('emplist')
    return render(request,'RegistrationEdit.html',{'emplist':emplist,'qualist':qualList,'deslist':desList})

@csrf_exempt
def qual(request):
    a=request.POST['fname']
    return render(request,'qualificationadd.html',{'name':a})

@csrf_exempt
def addproduct(request):
    if request.POST:
        
        adds=Category(categoryname=request.POST['cname'])
        adds.save()
        catid=adds.id
        i=1
        for i in range(10):
            key = "p" + str(i)
        
            if key in request.POST:
                pi=request.POST[key]
                if pi != '':
                    product=prodcuctcategory(catid_id=catid,productname=pi)
                    product.save()

    return render(request,'products.html')


def productlist(request):
    categories = Category.objects.all()

    details = []
    #product_category=""
    for i in categories:
        try:
            product_category = prodcuctcategory.objects.filter(catid_id=i.id)
            details.append({'category':i.categoryname})
            for item in product_category:
                details.append({ 'product_category':item})
        except prodcuctcategory.DoesNotExist:
             details.append({'category':i.categoryname, 'product_category':None})
    return render(request, 'productarray.html', {'details': details})

#using set method in html page 

"""def productlist(request):
    categories = Category.objects.all()
    return render(request,'productlist.html',{'categories':categories})
    """
def amlogout(request):
    auth.logout(request)
    return redirect('/accounts/login/')
def changepwd(request):
    return render(request,'changepwd.html')




   
   
    
