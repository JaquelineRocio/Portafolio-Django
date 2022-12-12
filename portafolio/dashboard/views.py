from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Item, VisitNumber,Userip, DayNumber
from django.utils import timezone
from dashboard.forms import NewItemForm

def change_info(request):       #Modificar información como visitas al sitio web y visitar ip
    # Por cada visita, agregue 1 al número total de visitas al sitio web
    count_nums = VisitNumber.objects.filter(id=1)   
    if count_nums:
        count_nums = count_nums[0]
        count_nums.count += 1
    else:
        count_nums = VisitNumber()
        count_nums.count = 1
    count_nums.save()

    # Registre el número de visitas a ip y cada ip
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # Obtener ip
        client_ip = request.META['HTTP_X_FORWARDED_FOR']
        client_ip = client_ip.split(",")[0]  # Así que aquí está la ip real
    else:
        client_ip = request.META['REMOTE_ADDR']  # Obtenga proxy ip aquí
    # print(client_ip)

    ip_exist = Userip.objects.filter(ip=str(client_ip))
    if ip_exist:  # Determinar si existe la ip
        uobj = ip_exist[0]
        uobj.count += 1
    else:
        uobj = Userip()
        uobj.ip = client_ip
        uobj.count = 1
    uobj.save()

    # Incrementar las visitas de hoy
    date = timezone.now().date()
    today = DayNumber.objects.filter(day=date)
    if today:
        temp = today[0]
        temp.count += 1
    else:
        temp = DayNumber()
        temp.dayTime = date
        temp.count = 1
    temp.save()
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard/index.html'
    extra_context = {
        "Items":Item.objects.all(),
        "Visits": VisitNumber.objects.count()
        }
    
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context["Items"] = Item.objects.all()
        context["Visits"] = VisitNumber.objects.count()
        change_info(self.request)
        return context

class CreateItemView(LoginRequiredMixin, FormView):
    model = Item
    template_name = "dashboard/create_item.html"
    form_class = NewItemForm

    def form_valid(self, form):
        Item.objects.create(**form.cleaned_data)
        return redirect("dashboard")
