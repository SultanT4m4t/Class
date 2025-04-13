import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from django.utils import timezone


# # Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, validators=[EmailValidator])
    usertype = models.CharField(max_length=8,  choices={"1": "Employer", "2":"Employee"}, null= False)


    def __str__(self):
        return f'username: {self.username} email:{self.email}'



class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employer')
    company_name = models.CharField(max_length=100)
    email = models.EmailField
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.company_name

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='employee')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

class JobListing(models.Model):
    company = models.ForeignKey(Employer, on_delete=models.CASCADE, related_name='joblisting')
    title = models.CharField(max_length=60)
    description = models.TextField
    currency = models.CharField(validators=[RegexValidator(regex='^[A-Z]{3}$')])
    salary = models.IntegerField
    remote = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.company} posted {self.title}'

class Application(models.Model):
    description = models.TextField
    job_listing = models.ForeignKey(JobListing, on_delete=models.CASCADE, related_name='applications')
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='applications')
    created_at = models.DateField(default=timezone.now)
    
    def __str__(self):
        return f'{self.job_listing} application successful'
