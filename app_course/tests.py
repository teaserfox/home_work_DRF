from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from app_course.models import Subscription


def test_subscribe_unsubscribe_course(self):
    """Тестирование подписки на урок"""

    # Данные о пользователе для подписки на курс
    data = {
        'user': self.user.pk,
    }

    # Отправка запроса на подписку на курс
    response = self.client.post(reverse('lms_platform:subscribe', args=[self.course.pk]), data=data)

    self.assertEqual(response.status_code, status.HTTP_201_CREATED)  # Проверка статуса ответа

    # Проверка наличия подписки на курс
    self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), True)

    # Отправка запроса на отписку от курса
    response = self.client.delete(reverse('lms_platform:unsubscribe', args=[self.course.pk]))

    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)  # Проверка статуса ответа

    # Проверка отсутствия подписки на курс
    self.assertEqual(Subscription.objects.filter(user=self.user, course=self.course).exists(), False)

