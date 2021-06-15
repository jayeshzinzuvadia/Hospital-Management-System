import os,re
from django.shortcuts import render
from doctor.models import Doctor
from patient.models import Patient,PatientComplaint
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.sessions.backends.db import SessionStore
from django.core.files.storage import FileSystemStorage

def loginController(request):
    if request.method=='POST':
        email=request.POST.get('email_id')
        passwd=request.POST.get('passwd')
        try:p1=Patient.objects.get(email_id=email)
        except Patient.DoesNotExist:p1=None
        try:p2=Doctor.objects.get(email_id=email)
        except Doctor.DoesNotExist:p2=None

        if(p1 is not None and passwd==p1.password):
            request.session['email']=email
            return HttpResponseRedirect(reverse('patient:patienthome'))
        if(p2 is not None and passwd==p2.password):
            request.session['email']=email
            return HttpResponseRedirect(reverse('doctor:doctorhome'))
        
        if request.session.get('email')!=email:
            return render(request,"view_login.html",{'invalidUser':'True'})

    return render(request,"view_login.html")

def logOutController(request):
    del request.session['email']
    return HttpResponseRedirect(reverse('loginApp:login'))

def newRegistration(request):
    if request.method=='POST':
        user=request.POST.get('user')
        name=request.POST.get('name')
        gender=request.POST.get('gender')
        phoneno=request.POST.get('phoneno')
        birthdate=request.POST.get('birthdate')
        address=request.POST.get('address')
        email=request.POST.get('email')
        passwd=request.POST.get('password')
        image_url='/images/default.png'
        if(request.FILES):
            image_url='/images/'+updateProfilePic(str(email),request.FILES['image_url'])
        if user=="Doctor":
            typeofdoctor=request.POST.get('typeofdoctor')
            degree=request.POST.get('degree')
            doctor=Doctor(name=name,gender=gender,phoneno=phoneno,
                img_url=image_url,typeofdoctor=typeofdoctor,degree=degree,
                birthdate=birthdate,email_id=email,password=passwd,hospital_address=address)
            doctor.save()
        else:
            patient=Patient(name=name,gender=gender,phoneno=phoneno,img_url=image_url,
                birthdate=birthdate,email_id=email,password=passwd,address=address)
            patient.save()
    return render(request,"view_login.html")

def updateProfilePic(email,f):
    for fl in os.listdir('hms/static/images'):
        if re.search("^("+email+").*$",fl):
            os.remove(os.path.join('hms/static/images',fl))
    fs=FileSystemStorage()
    fname=email+os.path.splitext(str(f))[1]
    fs.save(fname,f)
    return fname

def registrationController(request):
    return render(request,"loginApp:login")

def view_login(request):
    return render(request,"view_login.html")

def view_registration(request):
    return render(request,"view_registration.html")