from django.db import models

# Create your models here.
class Customer(models.Model):
    customercode = models.CharField(max_length = 255)
    customertype = models.CharField(max_length = 255)
    name = models.CharField(max_length = 255)
    locations = models.TextField()
    # contact = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()
