from django.shortcuts import render
from django.views.generic import ListView

from myapp.models import Student, Employee


class StudentView(ListView):
    model = Student

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['sequence'] = Student.objects.all().order_by('name')
        return context


class EmployeeView(ListView):
    model = Employee
    template_name = 'myapp/home.html'
    context_object_name = 'employees'

    def get_queryset(self):
        return Employee.objects.filter(eno='1')
