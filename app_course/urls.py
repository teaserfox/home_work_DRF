from app_course.apps import AppCourseConfig
from rest_framework.routers import DefaultRouter
from app_course.views import CourseViewSet, SubscriptionCreateAPIView, SubscriptionDestroyAPIView
from django.urls import path

app_name = AppCourseConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [
    path('course/<int:pk>/subscribe/', SubscriptionCreateAPIView.as_view(), name='subscribe'),
    path('course/<int:pk>/unsubscribe/', SubscriptionDestroyAPIView.as_view(), name='unsubscribe'),
] + router.urls
