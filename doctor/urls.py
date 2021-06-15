from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name='doctor'

urlpatterns=[
	path('',views.DoctorHome.as_view(),name='doctorhome'),
	path('writeprescription/',views.writePrescription,name='writeprescription'),
	path('doctorprofile/',views.DoctorProfile.as_view(),name='doctorprofile'),
	path('updatedoctor/',views.updateDoctor,name='updatedoctor'),
	path('scheduleappointments/',views.ScheduleAppointments.as_view(),name='scheduleappointments'),
	path('writeappointment/',views.writeAppointment,name='writeappointment'),
	path('checkedappointments/',views.CheckedAppointments.as_view(),name='checkedappointments'),
	path('cancelappointments/?P<case_id>',views.cancelAppointments,name='cancelappointments'),
]

if settings.DEBUG:
	urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)