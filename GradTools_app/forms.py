from django import forms
from .models import Department, Course, Purpose, Material


class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    dob=forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    age=forms.IntegerField()
    gender=forms.ChoiceField(choices=[('male','Male'),('female','Female')])
    phone_number=forms.CharField(max_length=15)
    email=forms.EmailField()
    address=forms.CharField(widget=forms.Textarea)
    department=forms.ModelForm(Department)
    courses=forms.ModelForm(Course)
    purpose=forms.ModelForm(Purpose)
    mateiral=forms.ModelForm(Material)


    # department=forms.ChoiceField[('artMain','Arts'),('bsMain','Biology Science'), ('comMain','Commerce'),('csMain','Computer Science'),('humMain','Humanities')]
    # courses=forms.ChoiceField[('bs01','Biotechnology'),('cs01','Computer Application'),('com01','Finance'),('hum01','History'),('cs02','IT'),('art02','Literature'),('art01','Music'),'bs02','Pharmacy']
    #


