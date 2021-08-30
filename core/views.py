from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import TemplateView
from .models import Mirror, Another

class Base(View):
    def get(self,request):
        return render(request, 'base.html')

class Home(View):
    def get(self,request):
        return render(request, 'home.html')

class Mirrors(TemplateView):
    template_name = 'core/mir.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mir = Mirror.objects.all()
        context.update({
            'mir': mir
        })
        return context


class Else(TemplateView):
    template_name = 'core/else.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        e = Another.objects.all()
        context.update({
            'e': e,
        })
        return context