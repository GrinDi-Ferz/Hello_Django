from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(max_length=250, verbose_name='Название')
    descript = models.TextField(blank=True)

class Measurement(models.Model):
    sensor_id = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', null=True)
    temperature = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Значение температуры')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Дата и время измерения')