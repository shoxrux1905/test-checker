from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User, StudyGroup
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserUpdateSerializer,
    UserUpdatePasswordSerializer,
    StudyGroupSerializer
)
from .permissions import IsAdminRole, IsTeacherRole



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



class UserLoginView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        refresh = RefreshToken.for_user(user)
        return Response({
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,
            },
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        })



class UserUpdateView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class UserUpdatePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdatePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class StudyGroupCreateView(generics.CreateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAdminRole]

class StudyGroupListView(generics.ListAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_admin:
            return StudyGroup.objects.all()
        elif user.is_teacher:
            return StudyGroup.objects.filter(teacher=user)
        else:
            return StudyGroup.objects.filter(students=user)

class StudyGroupDetailView(generics.RetrieveAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class StudyGroupUpdateView(generics.UpdateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsTeacherRole or IsAdminRole]

class StudyGroupArchiveView(generics.UpdateAPIView):
    queryset = StudyGroup.objects.all()
    serializer_class = StudyGroupSerializer
    permission_classes = [IsAdminRole]

    def update(self, request, *args, **kwargs):
        group = self.get_object()
        group.is_archived = True
        group.save()
        return Response({"detail": f"{group.name} arxivlandi."})