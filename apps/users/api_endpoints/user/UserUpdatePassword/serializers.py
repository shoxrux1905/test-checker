from rest_framework import serializers
from apps.users.models import User


class UserUpdatePasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(write_only=True)
    repeat_password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs['new_password'] != attrs['repeat_password']:
            raise serializers.ValidationError("Parollar bir xil emas.")
        return attrs

    def update(self, user, password):
        user.set_password(password['new_password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ["password"]
