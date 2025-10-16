from django.urls import path
from .views import SensorsView, SensorView, MeasurementsView, UpdateSensor
# from django.contrib import admin

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('sensors/', SensorsView.as_view()),
#     path('sensor/', SensorView.as_view()),
#     path('measurements/', MeasurementsView.as_view()),
#     path('update/', UpdateSensor.as_view())
#     # TODO: зарегистрируйте необходимые маршруты
# ]
urlpatterns = [
    path('sensors/', SensorsView.as_view()),  # список и создание
    path('sensor/<int:pk>/', SensorView.as_view()),  # получение/обновление/удаление конкретного
    path('measurements/', MeasurementsView.as_view()),
    path('sensor/<int:pk>/update/', UpdateSensor.as_view()),  # обновление по pk
]