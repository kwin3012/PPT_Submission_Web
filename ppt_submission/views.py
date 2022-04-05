from http.client import HTTPResponse
from ssl import HAS_TLSv1_1
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from ppt_submission.forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.contrib import messages
import json
# Create your views here.

def Topics(request):
    topics = Topic.objects.all()
    topics_json = json.dumps(list(Topic.objects.values()))
    return render(request,"topics.html",{"topics":topics,"topics_json":topics_json})

def add_topic(request):
    if request.method == 'POST':
        form = Topic_Form(request.POST)
        if form.is_valid():
            topic = form.cleaned_data['topic_name']
            topic = topic.lower()
            if Topic.objects.all().filter(topic_name=topic):
                messages.info(request,'Topic already taken!')
            else:
                t = Topic(topic_name = topic)
                t.save()
                messages.info(request,'Topic '+topic+' is added.')
                return redirect('topic')
                
        else:
            messages.error(request,'Something went wrong!')
    form = Topic_Form()
    context = {
        'form':form,
    }
    return render(request, 'add_topic.html', context)

def Index(request,id):
    students = Student.objects.all().filter(topic = id)
    topic = Topic.objects.get(id=id)
    add_student = True
    no_of_students = len(students)
    if no_of_students>=3:
        add_student = False

    return render(request,"students.html",{"id":id,"students":students,"add":add_student,"topic_name":topic.topic_name})

def add_student(request,id):
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            topic = Topic.objects.get(id=id)
            name=form.cleaned_data["name"]
            roll = form.cleaned_data["roll"]
            email = form.cleaned_data["email"]
            if Student.objects.all().filter(roll=roll):
                messages.error(request,"you are already selected a topic or have typed wrong roll number")
            else:
                student = Student(topic=topic,name=name,roll=roll,email=email)
                student.save()
                return redirect("index",id)
        else:
            messages.error(request, 'something went wrong!')

    form = Student_Form()
    context = {'form':form,}
    return render(request, 'add_student.html', context)

def add_file(request,id):
    if request.method == 'POST':
        form = File_Form(request.POST, request.FILES)
        if form.is_valid():
            roll = form.cleaned_data["roll_check"]
            if Student.objects.all().filter(roll=roll):
                if Student.objects.get(roll=roll).ppt_submitted == False:
                    if request.FILES['file']:
                        file = request.FILES['file']
                        fs = FileSystemStorage() #defaults to  MEDIA_ROOT  
                        filename = fs.save(file.name, file)
                        file_url = fs.url(filename)
                        student = Student.objects.get(roll=roll)
                        print(student.ppt_submitted)
                        student.ppt_submitted = True
                        student.save()
                        print(student.ppt_submitted)
                        f = File(student=student,roll_check=roll,file=filename)
                        f.save()
                        return redirect("index",id)
                    else:
                        messages.error(request,'unable to fetch your file.')
                else:
                    messages.error(request,'probably you are submitting your ppt at wrong place.')
            else:
                messages.error(request,'tying wrong roll number!')
        else:
            messages.error(request,'Something went wrong!')
        
    form = File_Form()
    context = {'form':form,}
    return render(request, 'add_file.html', context)


def download(request, roll):
    obj = File.objects.get(roll_check=roll)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response

    


    
    
    







    

