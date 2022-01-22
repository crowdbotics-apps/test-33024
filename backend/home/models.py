from django.conf import settings
from django.db import models


class Users(models.Model):
    "Generated Model"
    firstname = models.TextField()
