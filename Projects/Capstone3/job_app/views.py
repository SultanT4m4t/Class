import json
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import MyUser, MyEmployee, MyEmployer, JobPosting, JobApplication
from django.views.decorators.http import require_GET, require_POST, require_http_methods
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.core import serializers

# Create your views here.


@require_GET
#Welcome page
def home(request):
    return JsonResponse({'message':'Welcome to the JobPortal API'})


#Function to get User ID to put in Employer and Employee ID 
def userid(request):
    data = request.body
    dict_data = json.loads(data)
    email = dict_data.get('email')
    #Use .first to get a dict
    get_user = MyUser.objects.filter(email=email).values().first()
    if get_user == None:
        return None
    else:
        get_user_id=(get_user.get('id'))
        return get_user_id

# Function to get Employer ID to put in Job Posting. Employer model is a parent model for Job Posting
def employerid(request):
    id = userid(request)
    get_emp = MyEmployer.objects.filter(user_id=id).values().first()
    if get_emp == None:
        return None
    else:
        get_emp_id = get_emp.get("id")
        return get_emp_id
    
    

#Function to get Employee ID to put in Job Application. Employee model is a parent model for Job Application
def employeeid(request):
    id = userid(request)
    get_emp = MyEmployee.objects.filter(user_id=id).values().first()
    if get_emp == None:
        return None
    else:
        get_emp_id = get_emp.get("id")
        return get_emp_id


#testing if userid function works
def at(request):
    id = userid(request)
    get_emp = MyEmployee.objects.filter(user_id=id).values().first()
    if get_emp == None:
        return HttpResponse("Failed")
    else:
        get_emp_id = get_emp.get("id")
        return HttpResponse("Success")

#Decorators to control post request
@csrf_exempt
@require_POST

#Function based view 
def create_employee(request):
    data = request.body
    #Convert into Dict
    dict_data = json.loads(data)
    #Split dict into various values to create user and employee
    email = dict_data.get('email')
    first_name = dict_data.get('first_name')
    last_name = dict_data.get('last_name')
    username = dict_data.get('username')
    password = dict_data.get('password')
    new_user = MyUser.objects.create_user(email=email, username=username,password=password, usertype='Employee')
    new_employee = MyEmployee.objects.create(first_name=first_name, last_name=last_name, user_id=new_user.id)
    
    return JsonResponse({"message":"Employee Account created successfuly"}, status =201)



@csrf_exempt
@require_POST
def create_employer(request):
    data = request.body
    #Convert to Dict
    dict_data = json.loads(data)
    email = dict_data.get('email')
    username = dict_data.get('username')
    password = dict_data.get('password')
    company_name = dict_data.get('company_name')
    location = dict_data.get('location')
    new_user = MyUser.objects.create_user(email=email, username=username,password=password, usertype='Employer')
    new_employer = MyEmployer.objects.create(company_name=company_name, location=location, user_id=new_user.id)
    
    return JsonResponse({"message":"Employer Account created successfuly"}, status =201)



@csrf_exempt
@require_POST
def jobpost(request):
    emp_id = employerid(request)

    #Check if user is an employer
    if emp_id == None:
        return JsonResponse({'message':'User not allowed to post jobs'}, status = 401)
    else:
        data = request.body
        dict_data = json.loads(data)
        company_name = dict_data.get('company_name')
        title = dict_data.get('title')
        description = dict_data.get('description')
        currency = dict_data.get('currency')
        salary = dict_data.get('salary')
        dict_data.update({"employer_id":emp_id})
        dict_data.pop("email")
        posting = JobPosting.objects.create(**dict_data)
        return JsonResponse({'message':'Job Posting created successfully'}, status=201)


@csrf_exempt
@require_POST
def apply_job(request, job_id):
    emp_id = employeeid(request)
    #Checking if user is an employee
    if emp_id == None:
        return JsonResponse({'message':'User not an employee'}, status = 401)
    data = request.body
    dict_data = json.loads(data)
    resmue = dict_data.get('resume')
    dict_data.update({'applicant_id':emp_id})
    dict_data.update({'job_posting_id':job_id})
    dict_data.pop("email")
    apply = JobApplication.objects.create(**dict_data)
    return JsonResponse({'message': 'Appliction succesful'}, status = 201)

def job_listing(request):
    count = 0
    l = []
    all = JobPosting.objects.all()
    all = serializers.serialize('json',all)   
    all = json.loads(all)
    while count < len(all):
        for i in all:
            j = all[count].get('fields')
            count = count + 1
            l.append(j)
    return JsonResponse({'jobs': l})


def job_detail(request, job_id: int):
    job = JobPosting.objects.filter(id=job_id).first()
    json_job = serializers.serialize('json', [job])
    json_job = json.loads(json_job)
    display_json = json_job[0].get('fields')
    return JsonResponse({'job_details':display_json})

def application_details(request,job_id):
    app = JobApplication.objects.filter(job_posting_id=job_id)
    json_app = serializers.serialize('json', app)
    json_app = json.loads(json_app)
    display_json = json_app[0].get('fields')
    return JsonResponse({'applied':display_json})

def jobs_applied(request, applicant_id):
    applicant_id = employeeid(request)
    applied_jobs = JobApplication.objects.filter(applicant_id=applicant_id)
    print(applied_jobs)
    applied_jobs = serializers.serialize('json', applied_jobs)
    applied_jobs = json.loads(applied_jobs)
    display_json = applied_jobs[0].get('fields')
    return JsonResponse({'applied_jobs':display_json})
    # return HttpResponse("Hello")

