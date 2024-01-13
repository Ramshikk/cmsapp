
from django.contrib import admin
from django.urls import path,include
from django.conf import settings  
from django.conf.urls.static import static  

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('EditQualification/<int:itemid>',views.editqualification,name='edit'),
    path('qualificationlist',views.qualificationlist,name='quallist'),
    
     path('qualdelete/<int:itmid>',views.qualdelete,name='qualdelet'),

    path('addqualification/',views.addqualification,name='Addqual'),
    path('designation', views.adddesignation,name='adddes'),
    path('designationlist', views.designationlist,name='deslist'),
    path('designationedit/<int:itemid>', views.designationEdit,name='designationedit'),
    path('desdelete/<int:itemid>',views.designationDel,name="deldes"),
    path('classadd', views.classadd,name='classadd'),
    path('Division', views.division,name='division'),
    path('qualificationadd',views.qualad),
    path('studentregistration',views.studentreg,name='studreg'),
    path('studentlist',views.studentList,name='studlist'),

    path('studentedit',views.studentedit,name='studedit'),
    path('registration',views.empreg,name='empreg'),
    path('registrationlist',views.emplist,name='emplist'),
     path('registrationedit/<int:empid>',views.empedit,name='empedit'),
    path('qual',views.qual,name="kk"),

    path('product',views.addproduct),
    path('productlist',views.productlist),
    path('accounts/',include("django.contrib.auth.urls"),name="login"),
    path('logout',views.amlogout,name='log')
]
if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  
