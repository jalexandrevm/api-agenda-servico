from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.
@api_view(http_method_names=["GET", "POST"])
def agendamento_list_create(request):
    if request.method == "GET":
        # qs = Agendamento.objects.all() # mudar para apenas ativo
        qs = Agendamento.objects.filter(cancelado=False)
        serializer = AgendamentoSerializer(qs, many=True)
        return JsonResponse(serializer.data, safe=False)
    if request.method == "POST":
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            dado_validado = serializer.validated_data
            Agendamento.objects.create(
                data_horario = dado_validado["data_horario"],
                nome_cliente = dado_validado["nome_cliente"],
                email_cliente = dado_validado["email_cliente"],
                telefone_cliente = dado_validado["telefone_cliente"],
            )
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@api_view(http_method_names=["GET", "DELETE", "PUT", "PATCH"])
def agendamento_detail_delete_alter(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    if request.method == "DELETE":
        obj = get_object_or_404(Agendamento, id=id)
        # obj.delete() # alterado para apenas cancelar
        obj.cancelado = True
        obj.save()
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data, status=202)
    if request.method == "PUT":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data)
        if serializer.is_valid():
            dado_valido = serializer.validated_data
            obj.data_horario = dado_valido.get("data_horario", obj.data_horario)
            obj.nome_cliente = dado_valido.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = dado_valido.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = dado_valido.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(serializer.data, status=202)
        return JsonResponse(serializer.errors, status=400)
    if request.method == "PATCH":
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            dado_valido = serializer.validated_data
            obj.data_horario = dado_valido.get("data_horario", obj.data_horario)
            obj.nome_cliente = dado_valido.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = dado_valido.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = dado_valido.get("telefone_cliente", obj.telefone_cliente)
            obj.save()
            return JsonResponse(dado_valido, status=202)
        return JsonResponse(serializer.errors, status=400)
