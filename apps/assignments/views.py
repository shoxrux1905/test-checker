from rest_framework import generics, permissions, viewsets
from apps.assignments.models import Appeal
from .serializers import AppealSerializer
from .models import Assignment
from .serializers import AssignmentSerializer

class AppealListCreateView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all().order_by("-created_at")
    serializer_class = AppealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AppealDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [permissions.IsAuthenticated]


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_teacher:
            # Teacher sees only their assignments
            return Assignment.objects.filter(created_by=user)
        # Students see assignments in their groups
        return Assignment.objects.filter(group__students=user)
