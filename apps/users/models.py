from django.contrib.auth.models import AbstractUser
from django.db import models

from apps.common.models import BaseModel


class User(AbstractUser, BaseModel):
    is_teacher = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profiles/', null=True, blank=True)

    USER_ROLES = [
        ("admin", "Admin"),
        ("student", "Student"),
        ("teacher", "Teacher"),
    ]

    role = models.CharField(max_length=10, choices=USER_ROLES, default="student")
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_picture = models.ImageField(upload_to="profiles/", blank=True, null=True)

    class Meta:
        db_table = "users"

    def __str__(self):
        return f"{self.get_full_name()} ({self.get_role_display()})"

    @property
    def is_admin(self):
        return self.role == "admin"

    @property
    def is_student(self):
        return self.role == "student"

    @property
    def is_teacher(self):
        return self.role == 'teacher'


class StudyGroup(BaseModel):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE,related_name='teacher_groups')
    students = models.ManyToManyField(
        User, blank=True, related_name='student_groups',null=True
    )
    is_archived = models.BooleanField(default=False)

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return self.name
