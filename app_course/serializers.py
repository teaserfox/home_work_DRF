from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from app_course.models import Course
from app_lesson.models import Lesson


class CourseSerializer(serializers.ModelSerializer):
    """Сериализатор для модели курса"""
    class Meta:
        model = Course
        fields = '__all__'

    count_lessons = SerializerMethodField()  # Количество уроков
    lessons = SerializerMethodField()  # список уроков

    def get_count_lessons(self, course):
        """Метод для получения количества уроков в курсе"""

        return Lesson.objects.filter(course=course).count()

    def get_lessons(self, course):
        """Метод для получения списка всех уроков в курсе"""

        return [lesson.title for lesson in course.lesson_set.all()]

    class Meta:
        model = Course  # Модель
        fields = '__all__'  # ПОля

