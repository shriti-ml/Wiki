from django.db import models
from django import forms

# Create your models here.

class WikiInformation(models.Model):
	topic = models.CharField(max_length=150)
	article = models.TextField(default="")

	# def __str__(self):
	# 	return self.topic
