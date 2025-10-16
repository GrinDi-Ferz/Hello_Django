# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, SensorUpdateSerializer
from rest_framework import generics

class SensorsView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer