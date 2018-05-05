from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User)
	name = models.TextField()
	address = models.TextField()
	dob = models.TextField()
	encr_key = models.TextField()


class Patient_Id(models.Model):

	is_valid = models.BooleanField(default=False)


class Patient_Data(models.Model):
	doctor = models.TextField()
	date = models.TextField()
	symptoms = models.TextField()
	diagnosis = models.TextField()
	medicine = models.TextField()
	procedure = models.TextField()
	patient_id = models.ForeignKey(Patient_Id)