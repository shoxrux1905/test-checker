from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User, StudyGroup


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role=serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = [ 'username',  'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(username=data["username"], password=data["password"])
        if not user:
            raise serializers.ValidationError("Login yoki parol noto‘g‘ri.")
        if not user.is_active:
            raise serializers.ValidationError("Foydalanuvchi faol emas.")
        data["user"] = user
        return data


class UserUpdateSerializer(serializers.ModelSerializer):
    role=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ["username","role","first_name", "last_name", "email", "phone_number", "profile_picture"]

class UserUpdatePasswordSerializer(serializers.Serializer):
    # old_password = serializers.CharField(write_only=True)
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

class StudyGroupSerializer(serializers.ModelSerializer):
    teacher = UserRegisterSerializer(read_only=True)
    students = UserRegisterSerializer(many=True, required=False)

    class Meta:
        model = StudyGroup
        fields = ["name", "description", "teacher", "students", "is_archived", "created_at"]
