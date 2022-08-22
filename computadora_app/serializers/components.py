from rest_framework import serializers
from ..models.components import Mouse, Monitor, Keyboard, Speaker, MotherBoard, Processor

class MouseSerializer(serializers.ModelSerializer):
    """
    clase meta: decir que es lo que va a utilizar
    """
    class Meta:
        model = Mouse
        fields = '__all__'

class KeyboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Keyboard
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        fields = '__all__'

class SpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Speaker
        fields = '__all__'

class MotherboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoard
        fields = '__all__'

class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Processor
        fields = '__all__'