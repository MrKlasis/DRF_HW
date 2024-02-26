from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from school.models import Subscription, Course
from school.seriallizers.subscription import SubscriptionSerializer


class SubscriptionCreateAPIView(CreateAPIView):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user = request.user
        course_id = request.data.get('course_id')
        course_item = get_object_or_404(Course, id=course_id)

        # Получаем объект подписки пользователя на этот курс
        subs_item, created = Subscription.objects.get_or_create(user=user, course=course_item)

        if created:
            message = 'Подписка добавлена'
        else:
            subs_item.delete()
            message = 'Подписка удалена'

        return Response({"message": message})
