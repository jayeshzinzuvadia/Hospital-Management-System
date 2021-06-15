from django.conf import settings
from patient.models import Patient

def getPatientInfo(request):
	email=request.session.get('email')
	if(email is None):
		return {}
	try:
		p=Patient.objects.get(email_id=email)
		return {'patient_info':p}
	except Patient.DoesNotExist:
		return {}