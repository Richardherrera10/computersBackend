from rest_framework import serializers
from ..models.components import Mouse, Monitor, Keyboard, Speaker, MotherBoard, Processor
from ..models.computer import Computer

class ComputerSerializer(serializers.ModelSerializer):
    mouse = serializers.PrimaryKeyRelatedField(queryset = Mouse.objects.all())
    keyboard = serializers.PrimaryKeyRelatedField(queryset = Keyboard.objects.all())
    monitor = serializers.PrimaryKeyRelatedField(queryset = Monitor.objects.all())
    speaker = serializers.PrimaryKeyRelatedField(queryset = Speaker.objects.all())
    motherboard = serializers.PrimaryKeyRelatedField(queryset = MotherBoard.objects.all())
    processor = serializers.PrimaryKeyRelatedField(queryset = Processor.objects.all())
   # order_list = OrderSerializer(many = True, read_only= True)
    class Meta:
        model = Computer
        exclude = ('total_cost',)
        # fields = '__all__'
        depth = 1
        read_only_fields=('created_at', 'updated_at')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'total_cost': instance.total_cost,
            'quantity': instance.quantity,
            'mouse': {
                'id': instance.mouse.id
            },
            'keyboard': {
                'id': instance.keyboard.id
            },
            'monitor': {
                'id': instance.monitor.id
            },
            'speaker': {
                'id': instance.speaker.id
            },
            'motherboard': {
                'id': instance.motherboard.id
            },
            'processor': {
                'id': instance.processor.id
            }
        }