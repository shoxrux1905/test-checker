from django.db import models

from apps.common.models import BaseModel

class Group(BaseModel):
    course_name = models.CharField(max_length=255)
    course_number = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return self.course_name

class Teacher(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='teachers')
    
    def __str__(self):
        return f"Teacher : {self.first_name}"
    
class TeacherAssistant(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='teacher_assistants')
    
    def __str__(self):
        return f"Assistant : {self.first_name}"
    
class Student(BaseModel):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='students')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"