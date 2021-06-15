import os, re
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect,Http404
from django.core.files.storage import FileSystemStorage
from django.views import generic
from django.db.models import Q
from doctor.models import Doctor
from patient.models import Patient, PatientComplaint
from django.urls import reverse
# Create your views here.

class DoctorHome(generic.ListView):
    template_name = 'doctor/view_doctorhome.html'
    context_object_name = 'confirmed_appointment_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        return PatientComplaint.objects.filter(d_email=email,status='confirmed')

def writePrescription(request):
    email=request.session.get('email')
    if request.method == 'POST':
        prescription=request.POST.get('prescription','')
        case_id=request.POST.get('case_id','')
        d=PatientComplaint.objects.get(case_id=case_id)
        d.prescription=prescription
        d.status='checked'
        d.save()
        context_object_name = 'confirmed_appointment_list'
    return HttpResponseRedirect(reverse('doctor:doctorhome'))

class DoctorProfile(generic.ListView):
    template_name = 'doctor/view_doctorprofile.html'
    context_object_name = 'doctor_details'
    
    def get_queryset(self):
        email=self.request.session.get('email')
        return Doctor.objects.get(email_id=email)

def updateDoctor(request):
    email=request.session.get('email')
    if request.method == 'POST':
        phoneno=request.POST.get('phoneno','')
        hospital_address=request.POST.get('address','')
        d=Doctor.objects.get(email_id=email)
        if(request.FILES):
            d.img_url='/images/'+updateProfilePic(email,request.FILES['image'])
        d.phoneno=phoneno
        d.hospital_address=hospital_address
        d.save()
        context_object_name = {'doctor_details':d}
    return HttpResponseRedirect(reverse('doctor:doctorprofile'))

def updateProfilePic(email,f):
    for fl in os.listdir('hms/static/images'):
        if re.search("^("+email+").*$",fl):
            os.remove(os.path.join('hms/static/images',fl))
    fs=FileSystemStorage()
    fname=email+os.path.splitext(str(f))[1]
    fs.save(fname,f)
    return fname

class ScheduleAppointments(generic.ListView):
    template_name = 'doctor/view_scheduleappointments.html'
    context_object_name = 'patient_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        return PatientComplaint.objects.filter(d_email=email,status='pending')

def writeAppointment(request):
    email = request.session.get('email')
    reject=request.POST.get('reject',None)
    if request.method == 'POST':
        case_id=request.POST.get('case_id','')
        obj=PatientComplaint.objects.get(case_id=case_id)
        if reject==None:
            date = request.POST.get('date', '')
            time = request.POST.get('time', '')
            datetime=str(date)+" "+str(time)
            obj.appointmentdate=datetime
            obj.status='confirmed'
        else:
             obj.status='cancelled'
        obj.save()
    return HttpResponseRedirect(reverse('doctor:scheduleappointments'))

class CheckedAppointments(generic.ListView):
    template_name = 'doctor/view_checkedappointments.html'
    context_object_name = 'checked_appointment_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        return PatientComplaint.objects.filter(d_email=email,status='checked')

def cancelAppointments(request,case_id):
    if case_id != None:
        p=PatientComplaint.objects.get(pk=int(case_id))
        p.status='cancelled'
        p.save()
    return HttpResponseRedirect(reverse('doctor:doctorhome'))