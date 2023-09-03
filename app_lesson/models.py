from django.db import models
from app_course.models import Course
from users.models import NULLABLE


class Lesson(models.Model):
    """"Поля для модели урока, связанный с моделью:'app_course.Course"""
    title = models.CharField(max_length=150, verbose_name='название урока')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='lesson/', verbose_name='превью (картинка)', **NULLABLE)
    url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="курс")

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'
