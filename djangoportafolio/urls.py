
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import  path
from project import views
from user import views as user_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', views.home, name='home'),
    path('signup/', user_views.signup, name='signup'),
    path('projects/', views.projects, name='projects'),
    path('', user_views.signin, name='signin'),
    path('signin/', user_views.signin, name='signin'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create_project/', views.create_project, name='create_project'),
    path('projects/<int:project_id>', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/delete', views.delete_project, name='delete_project'),
    path("portafolio/<int:pk>/",user_views.UserDetailsTemplate.as_view(),name="portafolio")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)