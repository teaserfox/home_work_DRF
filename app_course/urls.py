from app_course.apps import AppCourseConfig
from rest_framework.routers import DefaultRouter
from app_course.views import CourseViewSet

app_name = AppCourseConfig.name


router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

urlpatterns = [

] + router.urls
