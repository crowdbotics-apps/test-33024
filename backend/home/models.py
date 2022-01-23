from django.conf import settings
from django.db import models


class Exam(models.Model):
    "Generated Model"
    name = models.TextField()
    createdate = models.DateField()
