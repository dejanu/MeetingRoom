from django.db import models

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=10,unique=True)
    capacity = models.IntegerField(default=1)
    status =  models.BooleanField(default=False)
    description = models.TextField()

    def __str__(self):
        return self.name
