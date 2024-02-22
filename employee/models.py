from django.db import models

class Department(models.Model):
    dept_name = models.CharField(max_length=500)
    no_of_employee = models.IntegerField()

    def __str__(self):
        return self.dept_name
    
class Employee(models.Model):
    firstname = models.CharField(max_length=500)
    lastname = models.CharField(max_length=500)
    emaill = models.CharField(max_length=500)
    passwordd = models.CharField(max_length=500)
    phone = models.BigIntegerField()
    address = models.TextField(max_length=500)
    job_title = models.TextField(max_length=500)
    salary = models.IntegerField()
    joined_date = models.DateField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname+' '+self.lastname
# Create your models here.
