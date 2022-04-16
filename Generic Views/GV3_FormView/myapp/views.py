from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm


# Create your views here.

class ContactFormView(FormView):
    form_class = ContactForm
    template_name = 'myapp/contact.html'
    success_url = 'success'

    # initial = {'name': "Nirajan", 'email': 'kcnirajan@gmail.com'}
    def form_valid(self, form):
        print(form.cleaned_data['name'])
        print(form.cleaned_data['email'])
        print(form.cleaned_data['message'])
        # return HttpResponse('Message sent')
        return super().form_valid(form)


class SuccessTemplateView(TemplateView):
    template_name = 'myapp/success.html'
