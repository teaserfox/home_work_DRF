from django.urls import path
from app_payment.apps import AppPaymentConfig
from app_payment.views import PaymentListAPIView, PaymentLessonCreateAPIView, PaymentCourseCreateAPIView, \
    confirm_payment

app_name = AppPaymentConfig.name

urlpatterns = [
    path('', PaymentListAPIView.as_view(), name='payment'),  # app_playment/
    path('lesson/payment/<int:pk>/', PaymentLessonCreateAPIView.as_view(), name='payment_create'),
    path('course/payment/<int:pk>/', PaymentCourseCreateAPIView.as_view(), name='payment_create'),
    path('confirm_payment/<int:pk>/', confirm_payment, name='payment_success')
]
