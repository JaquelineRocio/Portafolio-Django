from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout

from django.contrib.auth.models import User
from django.db import IntegrityError

from django.contrib.auth.decorators import login_required
from .models import Project

from .forms import ProjectForm

# Create your views here.

@login_required
def dashboard(request):
    current_user=request.user
    context={
        "proyectos": current_user.project_set.all(),
        
        "dashboard":"dashboard"
    }

    return render(request,"projects.html",context)

@login_required
def projects(request):
    projects = Project.objects.filter(user=request.user)
    current_user=request.user
    return render(request, 'projects.html', {"projects": projects, "cantidad":current_user.project_set.count(),
        "visitantes":current_user.visitanteportafolio_set.count(),})




@login_required
def create_project(request):
    if request.method == "GET":
        return render(request, 'create_project.html', {"form": ProjectForm})
    else:
        try:
            form = ProjectForm(request.POST, request.FILES)
            print(form)
            new_project = form.save(commit=False)
            new_project.user = request.user
            new_project.save()
            return redirect('projects')
        except ValueError:
            print(ValueError)
            return render(request, 'create_project.html', {"form": ProjectForm, "error": "Error creating project."})


def home(request):
    projects = Project.objects.filter(user=request.user)
    return render(request, 'home.html', {"projects": projects})


@login_required
def signout(request):
    logout(request)
    return redirect('home')




@login_required
def project_detail(request, project_id):
    if request.method == 'GET':
        project = get_object_or_404(Project, pk=project_id, user=request.user)
        
        form = ProjectForm(instance=project)
        return render(request, 'project_detail.html', {'project': project, 'form': form})
    else:
        try:
            project = get_object_or_404(Project, pk=project_id, user=request.user)
            form = ProjectForm(request.POST, instance=project)
            form.save()
            return redirect('projects')
        except ValueError:
            return render(request, 'project_detail.html', {'project': project, 'form': form, 'error': 'Error updating project.'})



@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, pk=project_id, user=request.user)
    if request.method == 'POST':
        project.delete()
        return redirect('projects')
