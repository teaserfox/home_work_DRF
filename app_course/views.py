from rest_framework.viewsets import ModelViewSet
from app_course.models import Course
from app_course.serializers import CourseSerializer

# Описание CRUD для моделей курса через ViewSets.


class CourseViewSet(ModelViewSet):
    """Набор представлений для модели курса"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
