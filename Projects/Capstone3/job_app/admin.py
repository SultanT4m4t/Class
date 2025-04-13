from django.contrib import admin
from .models import MyUser, MyEmployee, MyEmployer, JobApplication, JobPosting

# Register your models here.
admin.site.register(MyUser)
admin.site.register(JobPosting)
admin.site.register(JobApplication)
admin.site.register(MyEmployee)
admin.site.register(MyEmployer)