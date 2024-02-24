from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError

from school.models import Lesson
from school.validators import LessonVideoValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        permission_classes = [IsAuthenticated]
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validators = [LessonVideoValidator(field='video')]

    def validate(self, data):
        for validator in self.validators:
            fields_to_validate = validator.__fields__
            for field in fields_to_validate:
                if field not in data:
                    continue
                try:
                    validator(data)
                except ValidationError as e:
                    raise serializers.ValidationError({field: e.detail})
        return data
