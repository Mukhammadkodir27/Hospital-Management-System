from django.db import models

# Create your models here.


class Patient(models.Model):
    patient_Name = models.CharField(max_length=100)
    date_of_birth = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=100)
    gender = models.CharField(max_length=100)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.patient_Name
