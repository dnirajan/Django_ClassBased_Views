from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Student


class StudentDetailView(DetailView):
    model = Student
    template_name = 'myapp/detail.html'
    context_object_name = 'stu'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_student'] = self.model.objects.all().order_by('name')
        return context


class StudentListView(ListView):
    model = Student
    template_name = 'myapp/home.html'
    context_object_name = 'list'
