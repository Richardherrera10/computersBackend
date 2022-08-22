from django.db import models

from .computer import Computer

class Order(models.Model):
    order_code = models.CharField(max_length=100, unique=True)
    total_cost_order = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.order_code

class OrderDetailComputer(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    total_cost_order = models.FloatField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        result = self.decrement_computer_quantity()
        if type(result) == int or type(result) == float:
            self.total_cost_order = result * self.quantity
            print(self.total_cost_order)
            super(OrderDetailComputer, self).save(*args, **kwargs)
            return True
        else:
            raise Exception(result)

    def decrement_computer_quantity(self):
        computer_data = Computer.objects.get(id=self.computer.id)
        if computer_data.quantity > self.quantity:
            computer_data.quantity -= self.quantity
            computer_data.update_quantity(computer_data.quantity)
            return computer_data.total_cost
        else:
            return "No hay existencia"

    def __str__(self):
        return "self.computer.name"