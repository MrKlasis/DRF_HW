from rest_framework import serializers

from school.models import Payments, Course, Lesson


class PaymentsSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    lesson = serializers.PrimaryKeyRelatedField(queryset=Lesson.objects.all(), required=False)

    class Meta:
        model = Payments
        fields = ['id', 'pay', 'date', 'method', 'sessions_url', 'course', 'lesson', 'user']
