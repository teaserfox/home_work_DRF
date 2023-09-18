from rest_framework.fields import SerializerMethodField

from app_payment.models import Payment
from rest_framework import serializers

from app_payment.services import get_stripe_link


class PaymentSerializer(serializers.ModelSerializer):
    """Сериализатор модели Платеж"""

    payment_link = SerializerMethodField()  # Ссылка на оплату

    class Meta:
        model = Payment
        fields = '__all__'

    def get_payment_link(self, payment):
        """Метод для получения ссылки на оплату"""
        payment_link = get_stripe_link(payment)

        return payment_link


