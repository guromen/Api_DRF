from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=100, verbose_name='Описание')
    def __str__(self):
        return self.name


class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата измерения')
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')