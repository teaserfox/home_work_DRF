from rest_framework import generics
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from app_course.models import Course
from app_lesson.models import Lesson
from app_payment.models import Payment
from app_payment.serializers import PaymentSerializer


class PaymentListAPIView(generics.ListAPIView):
    """Класс-представление для вывода списка платежей"""

    serializer_class = PaymentSerializer  # класс-сериализатор
    queryset = Payment.objects.all()  # список платежей
    filter_backends = [DjangoFilterBackend, OrderingFilter]  # фильтры
    filterset_fields = ('course', 'lesson', 'payment_method')  # поля по которым можно фильтровать
    ordering_fields = ('payment_date',)  # Поля, по которым можно сортировать
    search_fields = ('course', 'lesson', 'payment_method')  # Поля, по которым можно производить поиск


class PaymentLessonCreateAPIView(generics.CreateAPIView):
    """Класс-представление для создания платежа для урока на основе Generics"""
    serializer_class = PaymentSerializer  # класс-сериализатор

    def perform_create(self, serializer, **kwargs):
        """Переопределение метода perform_create для добавления платежу информации о пользователе и уроке"""

        new_payment = serializer.save()  # создаем новый платеж
        new_payment.user = self.request.user  # добавляем авторизованного пользователя
        new_payment.lesson = Lesson.objects.get(id=self.kwargs['pk'])  # добавляем урок
        new_payment.save()  # сохраняем новый платеж
        new_payment.payment_amount = Lesson.objects.get(id=self.kwargs['pk']).price  # добавляем сумму платежа
        new_payment.save()  # сохраняем новый платеж


class PaymentCourseCreateAPIView(generics.CreateAPIView):
    """Класс-представление для создания платежа для курса на основе Generics"""
    serializer_class = PaymentSerializer  # класс-сериализатор

    def perform_create(self, serializer, **kwargs):
        """Переопределение метода perform_create для добавления платежу информации о пользователе, уроке и сумме"""

        new_payment = serializer.save()  # создаем новый платеж
        new_payment.user = self.request.user  # добавляем авторизованного пользователя
        new_payment.course = Course.objects.get(id=self.kwargs['pk'])  # добавляем урок
        new_payment.payment_amount = Course.objects.get(id=self.kwargs['pk']).price  # добавляем сумму платежа
        new_payment.save()  # сохраняем новый платеж


def confirm_payment(request, pk):
    """
    pk: айдишник платежа
    Подтверждение платежа на курс или урок
    """
    payment = Payment.objects.get(id=pk)  # получаем платеж из базы данных
    payment.is_confirm = True  # подтверждаем что он прошел
    payment.save()  # сохраняем платеж в базе данных

    if payment.course:
        payment.course.is_buy = True  # подтверждаем что курс оплачен
        payment.course.save()  # сохраняем курс в базе данных
    else:
        payment.lesson.is_buy = True  # подтверждаем что урок оплачен
        payment.lesson.save()  # сохраняем урок в базе данных

    # перенаправляем на страницу с успешным завершением платежа
    return render(request, 'app_payment/confirm_payment.html', {'payment': payment})
