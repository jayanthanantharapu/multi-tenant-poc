from django.db import models


class Patient(models.Model):
    name = models.CharField(max_length=100)


class PatientAddress(models.Model):
    patent_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
