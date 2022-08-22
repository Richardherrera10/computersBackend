from django.urls import path
from django.db import router

# django rest framework
from rest_framework.routers import DefaultRouter

# views
from .viewsets.components import MouseViewSet, KeyboardViewSet, MonitorViewSet, SpeakerViewSet, MotherboardViewSet, ProcessorViewSet
from .viewsets.computer import ComputerViewSet
from .viewsets.order import OrderViewSet, OrderDetailComputerViewSet
router = DefaultRouter()

# ruta y la vista que se encarga de responder al endpoint
# router.register(r'dispositivoEntrada', DispositivoEntradaViewSet)
router.register(r'mouse', MouseViewSet)
router.register(r'keyboard', KeyboardViewSet)
router.register(r'monitor', MonitorViewSet)
router.register(r'speaker', SpeakerViewSet)
router.register(r'motherboard', MotherboardViewSet)
router.register(r'processor', ProcessorViewSet)
router.register(r'computer', ComputerViewSet)
router.register(r'order', OrderViewSet)
router.register(r'orderdetailcomputer', OrderDetailComputerViewSet)
urlpatterns = router.urls


urlpatterns += [
  
]