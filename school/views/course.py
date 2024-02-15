from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from school.models import Course
from school.paginators import CoursePaginator
from school.permissions import IsOwner, IsModerator
from school.seriallizers.course import CourseSerializer
from school.tasks import curse_update_message


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_course = serializer.save(owner=self.request.user)

    def perform_update(self, serializer):
        obj = serializer.save()
        curse_update_message.delay(obj.id)

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAuthenticated, IsOwner]
        elif self.action in ['update', 'partial_update', 'destroy']:
            permission_classes = [IsOwner | IsModerator]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
