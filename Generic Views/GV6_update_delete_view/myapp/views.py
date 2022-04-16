from dataclasses import field, fields
from django import forms
from sre_constants import SUCCESS
from django.shortcuts import render
from django.views.generic.edit import UpdateView, CreateView,DeleteView
from .models import Student
from .forms import StudentForm
# Create your views here.
#inherits StudentForm from forms.py
class StudentCreateView(CreateView):
    form_class=StudentForm
    # fields=['name','email','password']
    template_name='myapp/create.html'
    success_url='/'
    
    # def get_form(self):
    #     form=super().get_form()
    #     form.fields['password'].widget=forms.PasswordInput()
    #     return form

#inherits Student Model form models.py    
class StudentUpdateView(UpdateView):
    model=Student
    fields=['name','email','password']
    template_name='myapp/create.html'
    success_url='/'
    
    def get_form(self):
        form=super().get_form()
        form.fields['password'].widget=forms.PasswordInput()
        return form
    
class StudentDeleteView(DeleteView):
    model=Student
    template_name='myapp/delete.html'
    success_url='/'