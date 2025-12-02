from rest_framework import serializers
from apps.users.models import StudyGroup
from apps.users.api_endpoints.user.UserRegister.serializers import UserRegisterSerializer


class StudyGroupSerializer(serializers.ModelSerializer):
    teacher = UserRegisterSerializer()
    students = UserRegisterSerializer(many=True, required=False)

    class Meta:
        model = StudyGroup
        fields = ["name", "description", "teacher", "students", "is_archived", "created_at"]
