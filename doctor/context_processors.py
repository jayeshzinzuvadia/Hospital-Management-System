from django.conf import settings
from doctor.models import Doctor

def getDoctorInfo(request):
	email=request.session.get('email')
	if(email is None):
		return {}
	try:
		d=Doctor.objects.get(email_id=email)
		return {'doctor_info':d}
	except Doctor.DoesNotExist:
		return {}