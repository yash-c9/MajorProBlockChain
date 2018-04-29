from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
	user = models.ForeignKey(User)
	name = models.TextField()
	address = models.TextField()
	dob = models.TextField()
	encr_key = models.TextField()


class DummyModel(models.Model):
	name = models.TextField()
	random_id = models.TextField()