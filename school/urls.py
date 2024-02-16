from django.urls import path, include
from rest_framework.routers import DefaultRouter
from school.views.course import CourseViewSet
from school.views.lesson import LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, LessonDestroyAPIView
from school.views.payments import PaymentsListAPIView, PaymentCreateAPIView
from school.views.subscription import SubscriptionCreateAPIView, SubscriptionDestroyAPIView

router = DefaultRouter()
router.register(r'courses', CourseViewSet)

lesson_patterns = [
    path('list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
    path('update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
]

urlpatterns = [
    path('lessons/', include((lesson_patterns, 'school'), namespace='lessons')),
    path('', include(router.urls)),
    path('payment_list/', PaymentsListAPIView.as_view(), name='payment_list'),
    path('payment/', PaymentCreateAPIView.as_view(), name='payment'),
    path('subscription/create', SubscriptionCreateAPIView.as_view(), name='subscription_create'),
    path('subscription/destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),
]
