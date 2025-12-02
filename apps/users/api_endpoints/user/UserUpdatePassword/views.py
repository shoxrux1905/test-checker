from rest_framework import generics, permissions

from apps.users.models import User
from .serializers import UserUpdatePasswordSerializer


class UserUpdatePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


__all__ = ["UserUpdatePasswordView"]
