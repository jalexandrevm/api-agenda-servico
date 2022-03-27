from django.contrib import admin
from django.urls import path

from agenda.views import agendamento_detail, agendamento_list

urlpatterns = [
    # path('agendamentos/', agendamento_list),
    path('agendamentos/', agendamento_list),
    path('agendamentos/', agendamento_create),
    path('agendamentos/<int:id>/', agendamento_detail),
    path('agendamentos/<int:id>/', agendamento_delete),
    path('agendamentos/<int:id>/', agendamento_alter),
]
