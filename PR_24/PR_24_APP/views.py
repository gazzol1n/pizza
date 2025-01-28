from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CapitalSerializer, CapitalListSerializer
from .models import Capital

class CapitalListView(APIView):
    def get(self, request):
        # Запрашиваем все записи о столицах из базы данных
        queryset = Capital.objects.all()

        # Добавим вывод для отладки
        print(f"Queryset size: {queryset.count()}")  # Выводим количество записей в базе данных

        # Сериализация с использованием CapitalListSerializer (обрабатывает набор данных)
        serializer_for_queryset = CapitalSerializer(             
            instance=queryset,  # Передаём набор записей             
            many=True # Указываем, что на вход подаётся набор записей 
        ) 


        # Сериализация с использованием CapitalSerializer (для одной записи)
        serializer_for_single = CapitalSerializer(
            instance=queryset.first()  # Берем только одну запись
        )

        # Покажем, какие данные у нас есть
        print(f"Single object serialized: {serializer_for_single.data}")
        print(f"Multiple objects serialized: {serializer_for_queryset.data}")

        # Показываем разницу между сериализацией одного объекта и множества
        return Response({
            'single_object_serialized': serializer_for_single.data,  # Результат сериализации одной записи
            'multiple_objects_serialized': serializer_for_queryset.data  # Результат сериализации набора записей
        })
