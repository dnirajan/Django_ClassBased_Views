from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'hoome.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['name']='Nirajan'
        context['roll'] = 28
        # context = {'name': 'Nirajan',
        #            'roll': 45}
        return context
