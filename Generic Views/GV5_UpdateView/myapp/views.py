from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from .models import Student


# Create your views here.
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    template_name = 'myapp/form.html'
    success_url = '/'


class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    template_name = 'myapp/form.html'
    success_url = '/'
