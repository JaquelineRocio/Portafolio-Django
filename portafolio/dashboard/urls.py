from django.urls import path
from .views import IndexView, CreateItemView

urlpatterns = [
    path('dashboard', IndexView.as_view(), name="dashboard"),
    path('create_item', CreateItemView.as_view(), name="create_item")
]