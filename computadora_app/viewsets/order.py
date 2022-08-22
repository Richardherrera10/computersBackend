from rest_framework import viewsets
from rest_framework.views import Response
from functools import reduce

from ..models.order import Order, OrderDetailComputer
from ..serializers.order import OrderSerializer, OrderDetailComputerSerializer

class OrderDetailComputerViewSet(viewsets.ModelViewSet):
    queryset = OrderDetailComputer.objects.all()
    serializer_class = OrderDetailComputerSerializer

    def create(self, request, *args, **kwargs):
        try:
            super().create(request, *args, **kwargs)
            return Response({'status': True, 'message': 'Order created successfully'})
        except Exception as e:
            return Response({'status': False, 'message': str(e)})
    

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def retrieve(self, request, *args, **kwargs):
        queryset = OrderDetailComputer.objects.filter(order_id=kwargs['pk'])
        serializer = OrderDetailComputerSerializer(queryset, many=True)    
        total_order = reduce(lambda x, y: x + y, [item['computer']['total_cost_order'] for item in serializer.data])
        order_data ={
            'id': queryset[0].order.id,
            'order_code': queryset[0].order.order_code,
            'order_details': serializer.data,
            'total_order': total_order
        }
        return Response(order_data)