from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .form import ContactForm


# RETURNING TEMPLATE AND CONTEXT
class MyView(View):
    def get(self, request):
        context = {'message': "Hi this is base view"}
        return render(request, 'home.html', context)


# DEALING WITH FORM
class ContactView(View):
    def get(self, request):
        fm = ContactForm()
        return render(request, 'contact.html', {'form': fm})

    def post(self, request):
        fm = ContactForm(request.POST)
        if fm.is_valid():
            print(fm.cleaned_data['name'])
            return HttpResponse("your form is submitted")
