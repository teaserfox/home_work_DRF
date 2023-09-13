from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app_course.models import Course, Subscription
from app_lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""
    class Meta:
        model = Course
        fields = '__all__'

    count_lessons = SerializerMethodField()  # Количество уроков
    lessons = SerializerMethodField()  # список уроков
    is_subscribed = SerializerMethodField()  # Проверка подписки

    def get_count_lessons(self, course):
        """Метод для получения количества уроков в курсе"""

        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        """Метод для получения списка всех уроков в курсе"""

        return [lesson.title for lesson in course.lesson_set.all()]

    def get_is_subscribed(self, course):
        """Метод для проверки подписки к курсу"""

        return Subscription.objects.filter(course=course, user=self.context['request'].user).exists()


class SubscriptionSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписки"""
    class Meta:
        model = Subscription
        fields = '__all__'

