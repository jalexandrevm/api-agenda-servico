from rest_framework import serializers

class AgendamentoSerializer(serializers.Serializer):
    # incluir atributos que serão serializados
    data_horario = serializers.DateField()
    nome_cliente = serializers.CharField(max_length=100)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length=100)
    pass
