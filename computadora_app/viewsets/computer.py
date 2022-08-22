from rest_framework.views import Response


from rest_framework import viewsets
from ..models.computer import Computer
from ..serializers.computer import ComputerSerializer

class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    
    def create(self, request, *args, **kwargs):
        instance = super().create(request, *args, **kwargs)
        response = instance.data
        if response['id'] is not None:
            return Response({'message': 'success', 'id': response})
        else:
            return Response({'message': 'falta stock'})