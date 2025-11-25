from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import UserRegisterSerializer
from apps.users.permissions import IsAdminRole


class UserRegisterView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [IsAdminRole]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user": serializer.data,
            "detail": "Foydalanuvchi muvaffaqiyatli yaratildi.",
        }, status=status.HTTP_201_CREATED)


__all__ = ["UserRegisterView"]
