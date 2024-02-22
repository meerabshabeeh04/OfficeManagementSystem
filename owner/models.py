from django.db import models

class Owner(models.Model):
    emaill = models.CharField(max_length=500)
    passwordd = models.CharField(max_length=500)

    def __str__(self):
        return self.emaill
# Create your models here.
