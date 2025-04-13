from django.contrib import admin
from .models import User, JobListing, Employee, Employer, Application

# Register your models here.
admin.site.register(User)
admin.site.register(JobListing)
admin.site.register(Application)
admin.site.register(Employee)
admin.site.register(Employer)