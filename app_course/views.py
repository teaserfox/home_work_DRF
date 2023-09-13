from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from app_course.models import Course, Subscription
from app_course.serializers import CourseSerializer, SubscriptionSerializer
from app_lesson.paginators import CoursePaginator
from app_lesson.permissions import IsNotModerator, IsOwnerOrModerator, IsOwner


# Описание CRUD для моделей курса через ViewSets.


class CourseViewSet(viewsets.ModelViewSet):
    """Класс-представление для модели Курс на основе viewsets"""

    serializer_class = CourseSerializer  # Класс-сериализатор
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        """Переопределение метода perform_create для добавления пользователя"""
        new_course = serializer.save()
        new_course.owner = self.request.user
        new_course.save()

    def get_permissions(self):
        """Переопределение метода get_permissions для назначения разных прав доступа на разные дейтсвия"""

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


class SubscriptionCreateAPIView(generics.CreateAPIView):
    """Класс-представление для подписки курс на основе Generics"""

    serializer_class = SubscriptionSerializer  # класс-сериализатор

    def perform_create(self, serializer, **kwargs):
        """Переопределение метода perform_create для добавления пользователя"""
        new_subscription = serializer.save()  # создаем новую подписку

        new_subscription.user = self.request.user  # добавляем авторизованного пользователя
        new_subscription.course = Course.objects.get(id=self.kwargs['pk'])  # добавляем курс
        new_subscription.save()  # сохраняем новую подписку


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    """Удаление подписки на курс на основе Generics"""

    queryset = Course.objects.all()  # список уроков

    def perform_destroy(self, instance, **kwargs):
        """Переопределение метода perform_destroy для удаления подписки на курс"""

        user = self.request.user
        # получаем подписку
        subscription = Subscription.objects.get(course_id=self.kwargs['pk'], user=user)

        subscription.delete()  # удаляем подписку
