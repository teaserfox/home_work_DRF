from rest_framework import generics
from app_lesson.models import Lesson
from app_lesson.permissions import IsNotModerator, IsOwnerOrModerator, IsOwner
from app_lesson.serializers import LessonSerializer


# Описание CRUD для моделей урока через Generic-классы.


class LessonCreateAPIView(generics.CreateAPIView):
    """ Cоздать урок """
    serializer_class = LessonSerializer

    # права доступа на добавление урока только для авторизованных пользователей, не входящих в группу модераторы
    permission_classes = [IsNotModerator]

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя созданному уроку"""
        new_lesson = serializer.save()
        new_lesson.owner = self.request.user
        new_lesson.save()


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

    # права доступа на редактирование урока только для его создателя или для пользователей, входящих в группу модераторы
    permission_classes = [IsOwnerOrModerator]


class LessonDestroyAPIView(generics.DestroyAPIView):
    """ Удалить урок по идентификатору """
    queryset = Lesson.objects.all()

    permission_classes = [IsOwner]  # права доступа на удаление урока только для его создателя
