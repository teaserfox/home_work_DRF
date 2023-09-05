from app_payment.models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Платеж"""

    class Meta:
        model = Payment
        fields = '__all__'
