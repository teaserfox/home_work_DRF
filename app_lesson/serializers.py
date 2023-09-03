from rest_framework import serializers
from app_lesson.models import Lesson


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
