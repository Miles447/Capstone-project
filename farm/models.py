from django.db import models

# Create your models here.
from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.species})"


class Produce(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="produce")
    produce_type = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    date_collected = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.produce_type} from {self.animal.name} - {self.quantity}"
