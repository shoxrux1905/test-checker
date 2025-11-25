from rest_framework import generics

from apps.users.models import StudyGroup
from apps.users.api_endpoints.study_group.StudyGroupListCreate.\
    serializers import StudyGroupSerializer
from apps.users.permissions import IsAdminOrReadOnly


class StudyGroupRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAdminOrReadOnly]


__all__ = ["StudyGroupRetrieveUpdateView"]
