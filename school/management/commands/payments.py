from django.core.management import BaseCommand

from school.models import Payments, CASH, Lesson, Course, TRANSFER
from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        payments_list = [
            {
                'pay': '1000',
                'lesson': Lesson.objects.get(pk=1),
                'user': User.objects.get(pk=2),
                'method': CASH,
                'date': "2023-11-24",
            },
            {
                'pay': '2000',
                'lesson': Lesson.objects.get(pk=4),
                'user': User.objects.get(pk=1),
                'method': TRANSFER,
                'date': "2023-11-25",
            },
            {
                'pay': '3000',
                'lesson': Lesson.objects.get(pk=5),
                'user': User.objects.get(pk=2),
                'method': CASH,
                'date': "2023-11-26",
            },
            {
                'pay': '4000',
                'course': Course.objects.get(pk=3),
                'user': User.objects.get(pk=2),
                'method': CASH,
                'date': "2023-11-27",
            },
            {
                'pay': '5000',
                'course': Course.objects.get(pk=3),
                'user': User.objects.get(pk=1),
                'date': "2023-11-28",
            },
            {
                'pay': '6000',
                'course': Course.objects.get(pk=1),
                'user': User.objects.get(pk=1),
                'date': "2023-11-29",
            },

        ]
        payment_for_create = []
        for pay in payments_list:
            payment_for_create.append(Payments(**pay))

        Payments.objects.all().delete()
        Payments.objects.bulk_create(payment_for_create)
