# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListCreateAPIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


#Создать датчик. Указываются название и описание датчика.
#Получить список датчиков. Выдаётся список с краткой информацией по датчикам: ID, название и описание.
class ListCreateSensor(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


#Изменить датчик. Указываются название и описание.
#Получить информацию по конкретному датчику. Выдаётся полная информация по датчику:
class RetrieveUpdateSensorApi(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


#Добавить измерение. Указываются ID датчика и температура.
class CreateMeasurementApi(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer