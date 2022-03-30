from django.contrib import admin
from django.urls import path

from agenda.views import agendamento_detail_delete_alter, agendamento_list_create

urlpatterns = [
    # path('agendamentos/', agendamento_list),
    path('agendamentos/', agendamento_list_create),
    path('agendamentos/<int:id>/', agendamento_detail_delete_alter),
]
