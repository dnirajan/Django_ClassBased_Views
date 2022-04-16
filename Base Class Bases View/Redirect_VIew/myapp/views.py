from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView


# Create your views here.
class SchoolRedirectView(RedirectView):
    url = 'https://www.w3schools.com/'
