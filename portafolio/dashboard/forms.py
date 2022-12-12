from django import forms

class NewItemForm(forms.Form):
    titulo = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        "class": "form-control mb-3"
    }))
    foto = forms.ImageField()
    descripcion = forms.CharField()
    tags = forms.CharField(max_length=100)
    url_github = forms.URLField(max_length=200)