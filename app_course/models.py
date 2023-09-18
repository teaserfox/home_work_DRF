from django.db import models
from config import settings
from users.models import NULLABLE

PAYMENT_CURRENCY_CHOIСES = [('usd', 'usd'), ('rub', 'rub')]  # Валюта платежей


class Course(models.Model):
    """Поля для модели курса"""

    title = models.CharField(max_length=150, verbose_name='название курса')
    preview = models.ImageField(upload_to='course/', verbose_name='превью (картинка)', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE)  # Пользователь
    price = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Стоимость курса', **NULLABLE)
    currency = models.CharField(max_length=20, choices=PAYMENT_CURRENCY_CHOIСES, verbose_name='Валюта', default='rub')
    is_buy = models.BooleanField(default=False)  # Показывает, куплен ли курс

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Subscription(models.Model):
    """Модель подписки"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь', **NULLABLE)
    course = models.ForeignKey(Course, verbose_name='Подписанный курс', on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
