from rest_framework import serializers

from school.models import Course
from school.seriallizers.lesson import LessonSerializer


class CourseSerializer(serializers.ModelSerializer):

    lesson_count = serializers.SerializerMethodField()
    lesson_list = LessonSerializer(source='lesson_set', many=True, read_only=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, instance):
        sub = instance.subscription.filter(user=self.context.get("request").user)
        if sub:
            return sub[0].is_active
        else:
            return False

    @staticmethod
    def get_lesson_count(instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ['pk', 'title', 'owner', 'lesson_count', 'subscription', 'lesson_list', 'price']
