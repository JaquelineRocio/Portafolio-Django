from django.forms import ModelForm
from .models import Project
from django import forms
class ProjectForm(ModelForm):
    title = forms.CharField(label="Titulo", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))

    descripcion=forms.CharField(label="Descripción",widget=forms.Textarea(attrs={'class': 'form-control',"rows":3}))

    tags = forms.CharField(label="Tags",max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

    foto_img = forms.ImageField(required=False,widget=forms.FileInput(attrs={'class': 'form-control'}))

    url_git = forms.URLField(label="Url de Git",widget=forms.URLInput(attrs={'class': 'form-control'}))

    class Meta:
        model=Project
        fields=['title','descripcion','tags','foto_img','url_git']

    def clean(self):
       cleaned_data = self.cleaned_data
       uploadedfile = cleaned_data.get("foto_img")
       
       if not uploadedfile:
           raise forms.ValidationError("Ingrese una foto")
       return cleaned_data 