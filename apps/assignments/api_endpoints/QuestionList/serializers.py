from rest_framework import serializers

from apps.assignments.models import Question
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class QuestionListSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'question_type', 'points', 'is_active', 'created_by']
            
__all__ = ['QuestionListSerializer']