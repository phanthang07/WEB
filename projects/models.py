from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 255)
    locations = models.CharField(max_length = 255)
    power = models.TextField()
    pv = models.TextField()
    transformer = models.TextField()
    hourlyData = models.TextField()
    dailyData = models.TextField()
    monthlyData = models.TextField()
    dashBoard = models.TextField()
    warning = models.TextField()
    history = models.TextField()
    project_password = models.CharField(max_length = 255)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return super().__str__()