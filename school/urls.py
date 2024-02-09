from django.urls import path
from school.apps import SchoolConfig
from school.views.course import CourseViewSet
from school.views.lesson import LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from school.views.payments import PaymentsListAPIView, PaymentCreateAPIView

app_name = SchoolConfig.name

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('course/create/', CourseViewSet.as_view({'post': 'create'}), name='course_create'),

    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('course/list/', CourseViewSet.as_view({'get': 'list'}), name='course_list'),

    path('lesson/retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('course/retrieve/<int:pk>/', CourseViewSet.as_view({'get': 'retrieve'}), name='course_retrieve'),

    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('course/update/<int:pk>/', CourseViewSet.as_view({'put': 'update'}), name='course_update'),

    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
    path('course/destroy/<int:pk>/', CourseViewSet.as_view({'delete': 'destroy'}), name='course_destroy'),

    path('payment_list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/', PaymentCreateAPIView.as_view(), name='payment_create'),
]
