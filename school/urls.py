from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school.views.course import CourseViewSet
from school.views.lesson import (
    LessonListAPIView,
    LessonRetrieveAPIView,
    LessonUpdateAPIView,
    LessonDestroyAPIView,
    LessonCreateAPIView,
)
from school.views.payments import PaymentsListAPIView, PaymentCreateAPIView, cancel_payment
from school.views.subscription import SubscriptionCreateDestroyAPIView
from school.apps import SchoolConfig

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lessons/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lessons/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('lessons/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lessons/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('', include(router.urls)),
    path('payment_list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/', PaymentCreateAPIView.as_view(), name='payment'),
    path('subscription/<int:pk>/', SubscriptionCreateDestroyAPIView.as_view(), name='subscription_create_destroy'),
    path('cancel_payment/', cancel_payment, name='cancel_payment'),
]
