from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='patient'
urlpatterns=[
	path('',views.PatientHome.as_view(),name='patienthome'),
	path('patientprofile/',views.PatientProfile.as_view(),name='patientprofile'),
	path('updatepatient/',views.updatePatient,name='updatepatient'),
	path('readnewappointment/',views.readnewappointment,name='readnewappointment'),
	path('createnewappointment/',views.CreateNewAppointment.as_view(),name='createnewappointment'),
	path('checkedappointments/',views.CheckedAppointments.as_view(),name='checkedappointments'),
	path('pendingappointments/',views.PendingAppointments.as_view(),name='pendingappointments'),
	path('cancelappointments/',views.cancelappointments,name='cancelappointments'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)