from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Room(models.Model):
	ROOM_CHOICE = (("SP","Simpleplay"),("MP","Multiplay"))
	name = models.CharField(max_length = 50)
	game_type = models.CharField(max_length=3, choices=ROOM_CHOICE)
	date_begin = models.DateField(auto_now = True)
	date_end = models.DateField(blank = True)
	def __str__(self):
		return self.name