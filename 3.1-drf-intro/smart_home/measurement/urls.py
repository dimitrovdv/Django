from django.urls import path

from measurement.views import RetrieveUpdateSensorApi, CreateMeasurementApi, ListCreateSensor

urlpatterns = [
    path('sensors/', ListCreateSensor.as_view()),
    path('sensor/<int:pk>/', RetrieveUpdateSensorApi.as_view()),
    path('measurement/', CreateMeasurementApi.as_view()),
]

