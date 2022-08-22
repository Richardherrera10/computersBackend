from rest_framework import serializers

from ..models.order import Order, OrderDetailComputer
from ..models.computer import Computer

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class OrderDetailComputerSerializer(serializers.ModelSerializer):
    computer = serializers.PrimaryKeyRelatedField(queryset=Computer.objects.all())
    order = serializers.PrimaryKeyRelatedField(queryset=Order.objects.all())
    class Meta:
        model = OrderDetailComputer
        fields = '__all__'
    
    def to_representation(self, instance):
        return {
            'computer':{
                'id': instance.computer.id,
                'name': instance.computer.name,
                'total_cost': instance.computer.total_cost,
                'quantity': instance.quantity,
                'total_cost_order': instance.total_cost_order
            },
            
        }
    