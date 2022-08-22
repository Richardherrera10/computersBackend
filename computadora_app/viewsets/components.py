from rest_framework.views import Response


from rest_framework import viewsets
from ..models.components import Mouse, Keyboard, Monitor, Speaker,MotherBoard, Processor
from ..serializers.components import MouseSerializer, KeyboardSerializer, MonitorSerializer, SpeakerSerializer, MotherboardSerializer, ProcessorSerializer
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter

# comment

class MouseViewSet(viewsets.ModelViewSet):
    queryset = Mouse.objects.all()
    serializer_class = MouseSerializer



class KeyboardViewSet(viewsets.ModelViewSet):
    queryset = Keyboard.objects.all()
    serializer_class = KeyboardSerializer


class MonitorViewSet(viewsets.ModelViewSet):
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class SpeakerViewSet(viewsets.ModelViewSet):
    queryset = Speaker.objects.all()
    serializer_class = SpeakerSerializer

class MotherboardViewSet(viewsets.ModelViewSet):
    queryset = MotherBoard.objects.all()
    serializer_class = MotherboardSerializer

class ProcessorViewSet(viewsets.ModelViewSet):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer