from rest_framework.viewsets import ModelViewSet
from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Набор представлений для пользовательской модели.
    Для создания необходимо ввести 'адрес электронной почты' и 'пароль'
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
