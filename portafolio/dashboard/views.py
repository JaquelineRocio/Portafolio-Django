from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Item
from dashboard.forms import NewItemForm

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'

class CreateItemView(LoginRequiredMixin, FormView):
    model = Item
    template_name = "dashboard/create_item.html"
    form_class = NewItemForm

    def form_valid(self, form):
        Item.objects.create(**form.cleaned_data)
        return redirect("dashboard")
