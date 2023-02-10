from sqlite3 import IntegrityError
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login,  authenticate
from user.forms import LoginForm,UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from ipware import get_client_ip
from user.models import VisitantePortafolio
# Create your views here.
def signin(request):
    if request.method == 'GET':
        return render(request, 'login.html', {"form": LoginForm})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {"form": LoginForm, "error": "Username or password is incorrect."})

        login(request, user)
        return redirect('dashboard')

def signup(request):
    if request.method == 'GET':
        return render(request, 'register.html', {"form": UserRegisterForm})
    else:

        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect('signin')
            except IntegrityError:
                return render(request, 'register.html', {"form": UserRegisterForm, "error": "Username already exists."})

        return render(request, 'register.html', {"form": UserRegisterForm, "error": "Passwords did not match."})

class UserDetailsTemplate(DetailView):
    model=User
    template_name='portafolio.html'
    context_object_name="usuario"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if context.get("usuario"):
            ip,is_routable=get_client_ip(self.request)
            usuario=context.get("usuario")
            if usuario.visitanteportafolio_set.filter(ipVisitante=ip).first() is None:
                ipBd=VisitantePortafolio(ipVisitante=ip,protafolioVisitado=usuario)
                ipBd.save()  
            context["proyectos"]=usuario.project_set.all()
           
        return context

