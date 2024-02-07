from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from school.models import Lesson
from school.validators import LessonVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        permission_classes = [IsAuthenticated]
        fields = '__all__'
        validators = [LessonVideoValidator(field='video')]
