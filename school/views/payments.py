from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from school.models import Payments, Course, Lesson
from school.seriallizers.payments import PaymentsSerializer
from school.service import product_create_stripe, price_create_stripe, session_create_stripe


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer

    def perform_create(self, serializer):
        new_pay = serializer.save()
        new_pay.user = self.request.user

        if course_id := self.request.data.get('course'):
            course = Course.objects.get(id=course_id)
            new_pay.pay = course.price
            prod_id = product_create_stripe(course.title)
            price_id = price_create_stripe(prod_id, new_pay.pay)
            new_pay.sessions_url = session_create_stripe(price_id)
        elif lesson_id := self.request.data.get('lesson'):
            lesson = Lesson.objects.get(id=lesson_id)
            new_pay.pay = lesson.price
            prod_id = product_create_stripe(lesson.title)
            price_id = price_create_stripe(prod_id, new_pay.pay)
            new_pay.sessions_url = session_create_stripe(price_id)
        new_pay.save()


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ('date',)
    permission_classes = [IsAuthenticated]
