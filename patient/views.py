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

class PatientHome(generic.ListView):
    template_name = 'patient/view_patienthome.html'
    context_object_name = 'confirmed_appointment_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        return PatientComplaint.objects.filter(p_email=email,status='confirmed')

class PatientProfile(generic.ListView):
    template_name = 'patient/view_patientprofile.html'
    context_object_name = 'patient_details'
    
    def get_queryset(self):
        email=self.request.session.get('email')
        return Patient.objects.get(email_id=email)

def updatePatient(request):
    email=request.session.get('email')
    if request.method == 'POST':
        phoneno=request.POST.get('phoneno','')
        address=request.POST.get('address','')
        p=Patient.objects.get(pk=email)
        if(request.FILES):
            p.img_url='/images/'+updateProfilePic(email,request.FILES['image'])
        p.phoneno=phoneno
        p.address=address
        p.save()
        context_object_name = {'patient_details':p}
    return HttpResponseRedirect(reverse('patient:patientprofile'))

def updateProfilePic(email,f):
    for fl in os.listdir('hms/static/images'):
        if re.search("^("+email+").*$",fl):
            os.remove(os.path.join('hms/static/images',fl))
    fs=FileSystemStorage()
    fname=email+os.path.splitext(str(f))[1]
    fs.save(fname,f)
    return fname

class CreateNewAppointment(generic.ListView):
    template_name = 'patient/view_createnewappointment.html'
    context_object_name = 'doctor_list'

    def get_queryset(self):
        return Doctor.objects.all()

def readnewappointment(request):
    p_email = Patient.objects.get(email_id=str(request.session.get('email')))
    d_email=request.POST.get('d_email',False)
    submit=request.POST.get('submit',False)
    chief_complaint=request.POST.get('chief_complaint',False)
    description=request.POST.get('description',False)

    if(d_email!=False and submit!=False):
        d_email=Doctor.objects.get(email_id=str(d_email))
        obj=PatientComplaint(p_email=p_email,d_email=d_email,
                             chief_complaint=chief_complaint,
                             description=description,
                             status='pending')
        obj.save()
    return HttpResponseRedirect(reverse('patient:createnewappointment'))

class CheckedAppointments(generic.ListView):
    template_name = 'patient/view_checkedappointments.html'
    context_object_name = 'checked_appointment_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        return PatientComplaint.objects.filter(p_email=email,status='checked')

class PendingAppointments(generic.ListView):
    template_name = 'patient/view_pendingappointments.html'
    context_object_name = 'pending_appointment_list'

    def get_queryset(self):
        email=self.request.session.get('email')
        list1=PatientComplaint.objects.filter( Q(p_email=email,status="pending") | Q(p_email=email,status="cancelled") )
        return list1

def cancelappointments(request):
    case_id=request.POST.get('cancel')
    p=PatientComplaint.objects.get(pk=case_id)
    p.delete()
    return HttpResponseRedirect(reverse('patient:pendingappointments'))