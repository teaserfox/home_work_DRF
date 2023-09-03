from rest_framework import generics
from app_lesson.models import Lesson
from app_lesson.serializers import LessonSerializer


# Описание CRUD для моделей урока через Generic-классы.
class LessonCreateAPIView(generics.CreateAPIView):
    """ Cоздать урок """
    serializer_class = LessonSerializer


class LessonListAPIView(generics.ListAPIView):
    """ Получить список уроков """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    """ Один урок по идентификатору """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(generics.UpdateAPIView):
    """ Редактировать урок по идентификатору """
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Удалить урок по идентификатору """
    queryset = Lesson.objects.all()
