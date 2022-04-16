from statistics import mode
from tkinter import Widget
from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','email','password']
        Widgets={'password':forms.PasswordInput()}