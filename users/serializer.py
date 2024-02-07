from rest_framework import serializers

from school.seriallizers.payments import PaymentsSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    payments = PaymentsSerializer(source='payments_set', many=True)

    class Meta:
        model = User
        fields = ('pk', 'email', 'payments')
