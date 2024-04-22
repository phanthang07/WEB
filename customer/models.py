from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length = 255)
    locations = models.CharField(max_length = 255)
    contact = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()
