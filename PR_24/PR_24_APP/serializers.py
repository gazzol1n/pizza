from rest_framework import serializers
from .models import Capital
from rest_framework.serializers import ListSerializer

# Дочерний сериализатор для одиночной записи
class CapitalSerializer(serializers.Serializer):
    capital_city = serializers.CharField(max_length=200)
    capital_population = serializers.IntegerField()
    author = serializers.CharField(source='author.username', max_length=200)

    @property
    def _readable_fields(self):
        """
        Это свойство возвращает только поля, которые не являются 'write_only'.
        """
        for field in self.fields.values():
            if not field.write_only:  # Исключаем поля, которые предназначены только для записи
                yield field

    def to_representation(self, instance):
        """
        Этот метод преобразует модель в словарь.
        """
        ret = super().to_representation(instance)
        # Дополнительная логика для представления
        return ret


# Кастомный сериализатор для работы с набором записей
class CapitalListSerializer(ListSerializer):
    child = CapitalSerializer()  # Указываем дочерний сериализатор для каждой записи

    @classmethod
    def many_init(cls, *args, **kwargs):
        """
        Метод many_init вызывает ListSerializer для обработки множества записей.
        """
        child_serializer = cls(*args, **kwargs)  # Создаем дочерний сериализатор
        list_kwargs = {'child': child_serializer}  # Передаем в ListSerializer
        meta = getattr(cls, 'Meta', None)
        list_serializer_class = getattr(meta, 'list_serializer_class', ListSerializer)
        return list_serializer_class(*args, **list_kwargs)


# Дополнительный класс Field, который будет использовать get_attribute
class Field(serializers.Field):
    def get_attribute(self, instance):
        """
        Этот метод извлекает атрибут из объекта (инстанса).
        """
        try:
            return getattr(instance, self.source_attrs[0])  # Используем getattr для получения атрибута
        except AttributeError:
            return None  # Если атрибут не найден, возвращаем None
