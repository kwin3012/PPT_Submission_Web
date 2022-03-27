from .models import *
from django import forms

class Topic_Form(forms.ModelForm):
    class Meta:
        model=Topic
        fields = '__all__' 

class Student_Form(forms.ModelForm):
    class Meta:
        model=Student
        fields = ["name","roll","email"]

class File_Form(forms.ModelForm):
    class Meta:
        model = File
        fields = ["roll_check","file"]



        


