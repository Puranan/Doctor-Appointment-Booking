from django.db import models

# Create your models here.
class contact(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    Email = models.EmailField(max_length=50)
    Contact = models.BigIntegerField()

    def __str__(self) -> str:
        return self.firstname

class texasapp(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    gender = models.CharField(max_length=50)
    age = models.CharField(max_length=50)
    Health_Issues = models.CharField(max_length=200)
    number = models.CharField(max_length=12)
    add = models.CharField(max_length=100)
    COLOR_CHOICES = (
        ('d', 'Select Doctor'),
        ('d1', 'Andrew'),
        ('d2', 'Senthil Kumar'),
        ('d3', 'Afsal'),
        ('d4', 'Vikram'),

    )
    sd = models.CharField(max_length=6, choices=COLOR_CHOICES, default='Select Doctor')
    def __str__(self) -> str:
        return self.name

class Andrew_Booking(models.Model):
    NAME1 = models.CharField(default=True, blank=True,max_length=10)

class Senthil_Booking(models.Model):
    NAME1 = models.CharField(default=True, blank=True,max_length=10)

class afsalas_Booking(models.Model):
    NAME1 = models.CharField(default=True, blank=True, max_length=10)
class vikram_Booking(models.Model):
    NAME1 = models.CharField(default=True, blank=True, max_length=10)