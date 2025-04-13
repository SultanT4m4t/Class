from django.urls import path
from job_app import views

urlpatterns = [
    path('', views.home),
    path('create-employee/',views.create_employee),
    path('create-employer/',views.create_employer),
    path('job-post/', views.jobpost),
    path('job-listing/', views.job_listing),
    path('job-detail/<int:job_id>/', views.job_detail),
    path('apply-job/<int:job_id>/', views.apply_job),
    path('<int:job_id>/applications/', views.application_details),
    path('<int:applicant_id>/jobs-applied/', views.jobs_applied),
    path('test/', views.at),
]