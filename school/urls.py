from django.urls import path

from school.apps import SchoolConfig
from school.views.course import CourseCreateAPIView, CourseListAPIView, CourseRetrieveAPIView, \
    CourseUpdateAPIView, CourseDestroyAPIView
from school.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDestroyAPIView
from school.views.payments import PaymentsListAPIView, PaymentCreateAPIView
from school.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = SchoolConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('course/create/', CourseCreateAPIView.as_view(), name='course_create'),

    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('course/list/', CourseListAPIView.as_view(), name='course_list'),

    path('lesson/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('course/retrieve/<int:pk>/', CourseRetrieveAPIView.as_view(), name='course_retrieve'),

    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('course/update/<int:pk>/', CourseUpdateAPIView.as_view(), name='course_update'),

    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('course/destroy/<int:pk>/', CourseDestroyAPIView.as_view(), name='course_destroy'),

    path('payment_list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/', PaymentCreateAPIView.as_view(), name='payment'),

    path('subscription/create', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),

]
