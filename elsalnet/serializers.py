from rest_framework import serializers
from .models import Company, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

    def update(self, instance, validated_data):
        # Переопределение метода update для запрета обновления поля 'debt_to_supplier'
        if 'debt_to_supplier' in validated_data:
            raise serializers.ValidationError("Обновление поля 'Задолженность (debt_to_supplier)' через API запрещено.")
        return super().update(instance, validated_data)

    def validate_supplier(self, value):
        if value and value.level not in [0, 1]:
            raise serializers.ValidationError(
                'Поставщик должен быть компанией с уровнем 0 или 1 (завод или розничная сеть).')
        return value
