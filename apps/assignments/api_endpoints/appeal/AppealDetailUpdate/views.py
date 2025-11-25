from rest_framework import generics, permissions
from apps.assignments.models import Appeal
from apps.assignments.api_endpoints.appeal.AppealListCreate.\
    serializers import AppealSerializer


class AppealDetailUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer
    permission_classes = [permissions.IsAuthenticated]


__all__ = ["AppealDetailUpdateView"]
