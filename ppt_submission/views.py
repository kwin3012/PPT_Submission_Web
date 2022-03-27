from http.client import HTTPResponse
from ssl import HAS_TLSv1_1
from django.shortcuts import render,redirect
from django.http import Http404, HttpResponse
from ppt_submission.forms import *
from .models import *
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.contrib import messages

# Create your views here.

def Topics(request):
    topics = Topic.objects.all()
    return render(request,"topics.html",{"topics":topics})

def add_topic(request):
    if request.method == 'POST':
        form = Topic_Form(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('topic')
        else:
            messages.error(request,'form detail invalid!')
    else:
        form = Topic_Form()
        context = {
            'form':form,
        }
    return render(request, 'add_topic.html', context)

def Index(request,id):
    students = Student.objects.all().filter(t=id)
    topic = Topic.objects.get(id=id)
    add=True
    n=len(students)
    if n>=3:
        add=False

    for i in range(n):
        if File.objects.filter(roll_check=students[i].roll):
            students[i].ppt_submitted = True

    return render(request,"students.html",{"id":id,"students":students,"add":add,"topic_name":topic.topic_name})

def add_student(request,id):
    if request.method == 'POST':
        form = Student_Form(request.POST)
        if form.is_valid():
            topic = Topic.objects.get(id=id)
            roll = form.cleaned_data["roll"]
            if Student.objects.all().filter(roll=roll):
                messages.error(request,"you are already register or have typed wrong roll number")
            else:
                student = Student(t=topic,name=form.cleaned_data["name"],roll=form.cleaned_data["roll"],email=form.cleaned_data["email"])
                student.save()
                return redirect("index",id)
        else:
            messages.error(request, 'student detail invalid!')

    
    form = Student_Form()
    context = {'form':form,}
    return render(request, 'add_student.html', context)

def add_file(request,id):
    if request.method == 'POST':
        form = File_Form(request.POST, request.FILES)
        if form.is_valid():
            rolls = form.cleaned_data["roll_check"]
            if Student.objects.all().filter(roll=rolls):
                print("heelo1")
                if Student.objects.get(roll=rolls).ppt_submitted == False:
                    print("help2")
                    print(rolls)
                    print(Student.objects.get(roll=rolls).ppt_submitted)
                    if request.FILES['file']:
                        file = request.FILES['file']
                        fs = FileSystemStorage() #defaults to  MEDIA_ROOT  
                        filename = fs.save(file.name, file)
                        file_url = fs.url(filename)
                        student = Student.objects.get(roll=rolls)
                        f = File(tt=student,roll_check=rolls,file=filename)
                        f.save()
                        return redirect("index",id)
                    else:
                        messages.error(request,'unable to fetch your file.')
                else:
                    messages.error(request,'probably you are submitting your ppt at wrong place.')
            else:
                messages.error(request,'tying wrong roll number!')
        else:
            messages.error(request,'file detail invalid!')
        
    form = File_Form()
    context = {'form':form,}
    return render(request, 'add_file.html', context)


def download(request, roll):
    obj = File.objects.get(roll_check=roll)
    filename = obj.file.path
    response = FileResponse(open(filename, 'rb'))
    return response

    


    
    
    







    

