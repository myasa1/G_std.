from django.db import models

from genders.models import GenderField
from django_contries.fiels import contryFiled
from address.models import AddressField


# Create your models here.
Gender=[('meil','meil'),('femeil','femeil')]
class Profile (models.Model):
    StdImage=models.ImageField(upload_to='profile/',blank=True,null=True)
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=50)
    StdID=models.AutoField()
    DateOfBirth=models.DateField(auto_now=False)
    currentAge=models.DecimalField(max_digits=5,decimal_places=2)
    Gender=GenderField()
    contry=contryFiled()
    cityStreet=models.CharField(max_length=50)
    PastalCode=models.DecimalField(max_digits=5,decimal_places=2)
    Eimal=models.CharField(max_length=50)
    PhonNum=models.DecimalField(max_digits=5,decimal_places=2)
    SecondaryRate=models.DecimalField(max_digits=5,decimal_places=2)
    MotherTongue=models.CharField(max_length=50)
    PaymentMethod=models.CharField(max_length=50)
    JoinDate=models.DateTimeField(auto_now=False)
    Massge=models.TextField(max_length=1000)
    address1=AdressField()
    address2=AddressField(related_name='+',blank=True,null=True)




    