from django.db import models
from .components import Monitor, Speaker, Mouse, Keyboard, Processor, MotherBoard
from django.db.models import F

class Computer(models.Model):
    name = models.CharField(max_length=50)
    mouse = models.ForeignKey(Mouse, on_delete=models.CASCADE)
    keyboard = models.ForeignKey(Keyboard, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    motherboard = models.ForeignKey(MotherBoard, on_delete=models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete=models.CASCADE)
    total_cost = models.FloatField(null=True, blank=True)
    quantity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'


    def save(self, *args, **kwargs):
        result_decrement = self.decrement_quantity()
        if type(result_decrement) == int or type(result_decrement) == float:
            self.total_cost = result_decrement
            super(Computer, self).save(*args, **kwargs)
            return True
        else:
            raise Exception(result_decrement)

    def decrement_quantity(self):
        cost = 0
        keyboard = Keyboard.objects.get(id=self.keyboard.id)
        mouse = Mouse.objects.get(id=self.mouse.id)
        display = Monitor.objects.get(id=self.monitor.id)
        speaker = Speaker.objects.get(id=self.speaker.id)
        motherBoard = MotherBoard.objects.get(id=self.motherboard.id)
        processor = Processor.objects.get(id=self.processor.id)
        #targeta = TargetaderReda.objects.get(id=self.targetader_reda.id)
    
        components = [keyboard, mouse, display, speaker, motherBoard, processor]
        
        quantity_less = [component for component in components if component.quantity < self.quantity]
        if len(quantity_less) > 0:
            component_less = {}
            for component in quantity_less:
                component_less[component.type_component] = component.quantity
            return component_less
        else:
            for component in components:
                cost += component.cost
                component.quantity -= self.quantity
                component.save()
            return cost

    def update_quantity(self, quantity):
        self.quantity = quantity
        super(Computer, self).save()

"""     def decrementar_cantidad(self):
        stockMonitor = Monitor.objects.filter(id=self.monitor.id)
        stockSPeaker = Speaker.objects.filter(id=self.speaker.id)
        stockMouse = Mouse.objects.filter(id=self.mouse.id)
        stockKeyboard = Keyboard.objects.filter(id=self.keyboard.id)
        stockProcessor = Processor.objects.filter(id=self.processor.id)
        stockMotherboard = MotherBoard.objects.filter(id=self.motherboard.id)

        if (stockMonitor[0].quantity > self.quantity and stockSPeaker[0].quantity > self.quantity and stockMouse[0].quantity > self.quantity and 
            stockKeyboard[0].quantity > self.quantity and stockProcessor[0].quantity > self.quantity and stockMotherboard[0].quantity > self.quantity):
            
            stockMonitor.update(quantity=F('quantity') - self.quantity)
            stockSPeaker.update(quantity=F('quantity') - self.quantity)
            stockMouse.update(quantity=F('quantity') - self.quantity)
            stockKeyboard.update(quantity=F('quantity') - self.quantity)
            stockProcessor.update(quantity=F('quantity') - self.quantity)
            stockMotherboard.update(quantity=F('quantity') - self.quantity)

            total = stockMonitor[0].cost + stockSPeaker[0].cost + stockMouse[0].cost +stockKeyboard[0].cost +stockProcessor[0].cost +stockMotherboard[0].cost
            
            return total
        else:
            return 0
    
    
    def save(self, *args, **kwargs):

        resultado = self.decrementar_cantidad()
        if resultado > 0:
            self.total_cost = resultado
            super(Computer, self).save(*args, **kwargs)
            return True
        else:
            return False

    def update_quantity(self, quantity):
        self.quantity = quantity
        super(Computer, self).save() """