from django.db import models


class Sensor(models.Model):

    name = models.CharField(max_length=50)
    description = models.TextField()


class Measurement(models.Model):

    temperature = models.FloatField()
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
