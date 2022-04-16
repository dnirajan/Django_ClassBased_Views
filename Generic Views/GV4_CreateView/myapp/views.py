from django.contrib import messages
from django.shortcuts import render
from django.views.generic import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from .models import Student
from .forms import StudentForm
from django import forms

'''
# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    template_name = 'myapp/create.html'
    # success_url = '/thank/'

    def get_form(self):
        form = super().get_form()
        form.fields['password'].widget = forms.PasswordInput()
        return form
'''


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'myapp/create.html'


class ThankTemplateView(TemplateView):
    template_name = 'myapp/thankyou.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/detail.html'
