from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Tweeter(models.Model):
	name = models.CharField(max_length=50)
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=25)
	password2 = models.CharField(max_length=25)
	def __str__(self):
		return self.username
	class Meta:
		db_table = 'Tweeters'
