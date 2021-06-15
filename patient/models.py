from django.db import models
from doctor.models import Doctor
# Create your models here.
class Patient(models.Model):
	email_id=models.EmailField(primary_key=True,max_length=30)
	password=models.CharField(max_length=20)
	name=models.CharField(max_length=30)
	gender=models.CharField(max_length=7)
	address=models.CharField(max_length=50)
	img_url=models.CharField(max_length=50)
	phoneno=models.IntegerField()
	birthdate=models.DateField('date of birth')

class PatientComplaint(models.Model):
	case_id=models.AutoField(primary_key=True)
	p_email=models.ForeignKey(Patient,on_delete=models.CASCADE)
	d_email=models.ForeignKey(Doctor,on_delete=models.CASCADE)
	chief_complaint=models.CharField(max_length=30)
	description=models.CharField(max_length=50)
	appointmentdate=models.DateTimeField(max_length=30)
	prescription=models.CharField(max_length=80)
	status=models.CharField(max_length=20)