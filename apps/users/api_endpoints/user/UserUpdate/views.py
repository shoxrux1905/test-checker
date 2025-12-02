from rest_framework import generics, permissions

from apps.users.models import User
from .serializers import UserUpdateSerializer
from apps.users.permissions import IsTeacherRole


class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


__all__ = ["UserUpdateView"]
