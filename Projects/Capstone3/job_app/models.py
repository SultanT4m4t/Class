from datetime import timedelta
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import EmailValidator, RegexValidator
# Create your models here.

class MyUser(AbstractUser):
    email = models.EmailField(validators=[EmailValidator], unique=True, null=False)
    usertype = models.CharField(max_length=8)

    REQUIRED_FIELDS = ['email','usertype','password']

    def __str__(self): 
        return f'{self.username} {self.email}'
    

class MyEmployee(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='myemployee')
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    description=models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {MyUser.email}'
    
class MyEmployer(models.Model):
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE, related_name='employer')
    company_name = models.CharField(max_length=100, null=False)
    location = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.company_name
    
class JobPosting(models.Model):
    employer = models.ForeignKey(MyEmployer, on_delete=models.CASCADE, related_name='joblisting')
    company_name = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=60, null=False)
    description = models.TextField(blank=True)
    currency = models.CharField(blank=True, validators=[RegexValidator(regex='^[A-Z]{3}$')])
    salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    remote = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    deadline = models.DateField(default=(timezone.now() + timedelta(days=90)) ,null=True)

    def __str__(self):
        return f'Company: ({self.company_name}) Position: ({self.title})'

class JobApplication(models.Model):
    job_posting = models.ForeignKey(JobPosting, on_delete=models.CASCADE, related_name='job_application')
    applicant = models.ForeignKey(MyEmployee, on_delete=models.CASCADE, related_name='job_application')
    resume = models.TextField(null=False)
    applied_at = models.DateField(default=timezone.now)

    def __str__(self):
        return f'{self.applicant.first_name} {self.applicant.last_name} applied for {self.job_posting.title}'