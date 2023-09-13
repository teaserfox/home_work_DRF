from rest_framework import serializers
from app_lesson.models import Lesson
from app_lesson.validators import LinkToVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для модели урока"""
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [LinkToVideoValidator('link_to_video')]
