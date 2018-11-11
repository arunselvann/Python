from django.db import models

class user(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
