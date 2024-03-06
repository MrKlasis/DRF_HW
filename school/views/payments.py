from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated

from school.models import Payments, Course, Lesson
from school.seriallizers.payments import PaymentsSerializer
from school.service import product_create_stripe, price_create_stripe, session_create_stripe


class PaymentCreateAPIView(CreateAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    permission_classes = [IsAuthenticated]

    @staticmethod
    def extract_session_id(session_url):
        parts = session_url.split('/')
        return parts[-1] if parts else None

    def perform_create(self, serializer):
        new_pay = serializer.save()
        new_pay.user = self.request.user

        course_id = self.request.data.get('course')
        lesson_id = self.request.data.get('lesson')

        if course_id:
            course = get_object_or_404(Course, id=course_id)
            new_pay.pay = course.price
            prod_id = product_create_stripe(course.title)
            price_id = price_create_stripe(prod_id, new_pay.pay)
            session_url = session_create_stripe(price_id)
            new_pay.sessions_url = session_url
            new_pay.stripe_session_id = PaymentCreateAPIView.extract_session_id(session_url)
            new_pay.course = course
            course.stripe_product_id = prod_id
            course.save()
        elif lesson_id:
            lesson = get_object_or_404(Lesson, id=lesson_id)
            new_pay.pay = lesson.price
            prod_id = product_create_stripe(lesson.title)
            price_id = price_create_stripe(prod_id, new_pay.pay)
            session_url = session_create_stripe(price_id)
            new_pay.sessions_url = session_url
            new_pay.stripe_session_id = PaymentCreateAPIView.extract_session_id(session_url)
            new_pay.lesson = lesson
            lesson.stripe_product_id = prod_id
            lesson.save()

        new_pay.save()


class PaymentsListAPIView(ListAPIView):
    queryset = Payments.objects.all()
    serializer_class = PaymentsSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['course', 'lesson', 'method']
    ordering_fields = ('date',)
    permission_classes = [IsAuthenticated]


@api_view(['GET'])
def cancel_payment(request):
    # Обработчик для отмены платежа
    return Response({"detail": "Payment canceled."})
