from django.db import models

class Component(models.Model):
    
    component = (
        ('keyboard', 'teclado'),
        ('mouse', 'raton'),
        ('monitor', 'monitor'),
        ('speaker', 'altavoz'),
        ('motherboard', 'placa'),
        ('processor', 'procesador')
    )
    component_type = models.CharField(max_length=20, choices = component, null=True)
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.component_type


class InternalDevice(Component):
    brand = models.CharField(max_length=150)

    def __str__(self):
        return self.brand


class MotherBoard(InternalDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.descriptoin}'

class Processor(InternalDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.descriptoin}'

class OutputDevice(Component):
    brand = models.CharField(max_length=150)

    def __str__(self):
        return self.brand


class Speaker(OutputDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.descriptoin}'

class Monitor(OutputDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.descriptoin}'  

class InputDevice(Component):
    brand = models.CharField(max_length=150)

    def __str__(self):
        return self.brand 

class Mouse(InputDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'{self.id} - {self.descriptoin}'


class Keyboard(InputDevice):
    quantity = models.IntegerField()
    cost = models.IntegerField()
    descriptoin = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id} - {self.descriptoin}'