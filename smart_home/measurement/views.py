from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView
from .models import Measurement, Sensor
from .serializers import SensorSerializer, MeasurementSerializer
from rest_framework.response import Response
from django.forms import model_to_dict


class SensorsView(ListAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        new_data = request.data
        sensor = SensorSerializer(data=new_data)
        if sensor.is_valid():
            sensor.save()
            return Response(f'Датчик создан: {sensor.data}')
       
        
class SensorIdView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def patch(self, request, pk):
        sensor = Sensor.objects.get(id=pk)
        sensor.description = request.data['description']
        sensor.save()
        return Response({sensor.name :sensor.description})
    
class MeasureCreateView(ListCreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        new_measure = Measurement.objects.create(
            sensor=Sensor.objects.get(id=request.data['sensor']),
            temperature=request.data['temperature'],
        )
        return Response(f'Температура: {new_measure.temperature} \
                          Время измерения: {new_measure.created_at}')
