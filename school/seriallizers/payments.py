from rest_framework import serializers

from school.models import Payments
from school.seriallizers.course import CourseSerializer
from school.seriallizers.lesson import LessonSerializer


class PaymentsSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Payments
        fields = ['id', 'pay', 'date', 'method', 'sessions_url', 'course', 'lesson', 'user']
