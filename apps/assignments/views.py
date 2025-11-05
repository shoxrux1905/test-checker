from rest_framework import generics, permissions
from apps.assignments.models import Appeal
from .serializers import AppealSerializer

class AppealListCreateView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all().order_by('-created_at')
    serializer_class = AppealSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)


class AppealDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [permissions.IsAuthenticated]
