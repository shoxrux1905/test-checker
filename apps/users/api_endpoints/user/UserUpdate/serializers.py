from rest_framework import serializers
from apps.users.models import User


class UserUpdateSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ["username","role","first_name",
                  "last_name", "email", "phone_number", "profile_picture"]
