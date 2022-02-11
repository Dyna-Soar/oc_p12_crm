from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# Add a custom Choice field for interest_level
# Create contract_pdf directory
# Set matching order of classes


class User(AbstractUser):

    def __str__(self):
        return f'{self.username}'


class Manager(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)


class Prospect(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    # Add a custom Choice field for interest_level
    interest_level = models.CharField(max_length=30, blank=True)


class SalesEmployee(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    prospects = models.ManyToManyField(Prospect, blank=True)


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    company_name = models.CharField(max_length=50)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(blank=True)
    sales_contact = models.ForeignKey(SalesEmployee, on_delete=models.PROTECT)


class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    sales_employee = models.ForeignKey(SalesEmployee, on_delete=models.PROTECT)
    date_signed = models.DateField(blank=True)
    signed = models.BooleanField(default=False)
    price = models.IntegerField()
    pdf = models.FileField(upload_to='contracts_files/', blank=True)


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
    date_start = models.DateTimeField()
    date_end = models.DateTimeField()
    location = models.CharField(max_length=200)
    comments = models.TextField(max_length=300, blank=True)


class SupportEmployee(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    events = models.ManyToManyField(Event, blank=True)
