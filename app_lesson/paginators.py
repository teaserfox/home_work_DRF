from rest_framework.pagination import PageNumberPagination

from app_course.models import Course
from app_lesson.models import Lesson


class CoursePaginator(PageNumberPagination):
    """Класс-пагинатор для вывода всех курсов на одной странице"""

    page_size = len(Course.objects.all())


class LessonPaginator(PageNumberPagination):
    """Класс-пагинатор для вывода всех уроков на одной странице"""

    page_size = len(Lesson.objects.all())
