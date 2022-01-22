from django.conf import settings
from django.db import models


class Users(models.Model):
    "Generated Model"
    firstname = models.TextField()


class Exam(models.Model):
    "Generated Model"
    name = models.TextField()
    createdate = models.DateField()
