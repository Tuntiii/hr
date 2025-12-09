from django.db import models

class Employee(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    job_title=models.TextField(max_length=100)
    salary=models.IntegerField()
 
# Create your models here.
