from django.db import models

class Member(models.Model):
	firstname = models.CharField(max_length=255, null=False, blank=False)
	lastname = models.CharField(max_length=255, null=False, blank=False)
	phone = models.IntegerField(null=False, blank=False)
	joined_date = models.DateField(null=False, blank=False)
	hobbies = models.TextField(blank=False, null=False)
# Create your models here.



