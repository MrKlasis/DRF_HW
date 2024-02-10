from rest_framework import serializers

from school.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = ['pk', 'user', 'course', 'is_active']
