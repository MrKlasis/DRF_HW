from rest_framework import serializers
from school.seriallizers.payments import PaymentsSerializer
from users.models import User
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    payments = PaymentsSerializer(source='payments_set', many=True, read_only=True)

    class Meta:
        model = User
        fields = ('pk', 'email', 'password', 'payments')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(
            email=validated_data['email'],
            password=make_password(password)
        )
        return user
