
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('name=Rekruto&message=Давайдружить!',views.next, name='Rekruto&message=Давайдружить!')
]
