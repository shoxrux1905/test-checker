from rest_framework import generics

from apps.users.models import StudyGroup
from .serializers import StudyGroupSerializer
from apps.users.permissions import IsAdminOrReadOnly


class StudyGroupListCreateView(generics.ListCreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAdminOrReadOnly]


    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return StudyGroup.objects.all()
        elif user.is_teacher:
            return StudyGroup.objects.filter(teacher=user)


__all__ = ["StudyGroupListCreateView"]
