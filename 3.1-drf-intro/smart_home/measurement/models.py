from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)

class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.name} - {self.description}'

class Measurement(models.Model):
    temperature = models.FloatField(verbose_name='Температура')
    date_of = models.DateTimeField(auto_now_add=True, verbose_name='Время измерения')
    sensor = models.ForeignKey('Sensor', on_delete=models.CASCADE, related_name='measurements')