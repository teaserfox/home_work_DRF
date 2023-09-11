from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from app_course.models import Course
from app_course.serializers import CourseSerializer
from app_lesson.permissions import IsNotModerator, IsOwnerOrModerator, IsOwner


# Описание CRUD для моделей курса через ViewSets.


class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для модели Курс на основе viewsets"""

    serializer_class = CourseSerializer  # Класс-сериализатор
    queryset = Course.objects.all()

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """Переопределение метода get_permissions для назначение разных прав доступа на разные дейтсвия"""

        # просматривать список уроков и детальную информацию по ним может любой авторизованный пользователь
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]

        # создавать курсы может только пользователь, не входящий в группу модераторы
        elif self.action == 'create':
            permission_classes = [IsAuthenticated, IsNotModerator]

        # редактировать курсы может только создатель курса или модератор
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [IsAuthenticated, IsOwnerOrModerator]

        # удалять курсы может только их создатель
        elif self.action == 'destroy':
            permission_classes = [IsAuthenticated, IsOwner]

        return [permission() for permission in permission_classes]
