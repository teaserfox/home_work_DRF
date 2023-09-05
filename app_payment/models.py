from django.db import models
from app_course.models import Course
from app_lesson.models import Lesson
from config import settings
from users.models import NULLABLE

PAYMENT_METHOD_CHOICES = [('Cash', 'Наличные'), ('money_transfer', 'денежный перевод')]


class Payment(models.Model):
    """Модель платежа"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT, verbose_name='Пользователь')
    payment_date = models.DateTimeField(auto_now=True, verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, verbose_name='Оплаченный курс', on_delete=models.SET_NULL, **NULLABLE)
    lesson = models.ForeignKey(Lesson, verbose_name='Оплаченный урок', on_delete=models.SET_NULL, **NULLABLE)
    payment_amount = models.DecimalField(max_digits=20, decimal_places=3, verbose_name='Сумма оплаты')
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, verbose_name='Способ оплаты')

    def __str__(self):
        return f'{self.user} {self.payment_amount} ({self.payment_method})'

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
