from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    

