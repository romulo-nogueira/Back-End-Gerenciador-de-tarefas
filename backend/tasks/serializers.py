from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        # O usuário não será enviado no body do JSON, será pego do token logado
        read_only_fields = ['user'] 

    def validate(self, data):
        """
        Regra de negócio: A data de entrega não pode ser anterior à data de início.
        """
        data_inicio = data.get('data_inicio')
        data_entrega = data.get('data_entrega')

        if data_inicio and data_entrega and data_entrega < data_inicio:
            raise serializers.ValidationError({
                "data_entrega": "A data de término não pode ser anterior à data de início."
            })
        
        return data