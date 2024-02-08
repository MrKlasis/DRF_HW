from rest_framework import viewsets
from school.models import Course
from school.seriallizers.course import CourseSerializer
from school.permissions import IsOwner, IsModerator
from rest_framework.permissions import IsAuthenticated


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.action in ['update', 'partial_update', 'destroy']:
            self.permission_classes = [IsOwner | IsModerator]
        return super().get_permissions()
