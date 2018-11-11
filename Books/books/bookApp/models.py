from django.db import models
from passlib.hash import pbkdf2_sha256 as e

class User(models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Email = models.EmailField(max_length=254)
    Password = models.CharField(max_length=254)

    objects = models.Manager()

    def __str__(self):
        return self.Email

    def verify_password(self, password):
        return e.verify(password, self.Password)