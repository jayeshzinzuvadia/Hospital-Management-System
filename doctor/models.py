from django.db import models

# Create your models here.
class Doctor(models.Model):
	email_id=models.CharField(primary_key=True,max_length=30)
	password=models.CharField(max_length=20)
	name=models.CharField(max_length=30)
	gender=models.CharField(max_length=7)
	img_url=models.CharField(max_length=50)
	typeofdoctor=models.CharField(max_length=20)
	degree=models.CharField(max_length=30)
	hospital_address=models.CharField(max_length=50)
	phoneno=models.IntegerField()
	birthdate=models.DateField('date of birth')