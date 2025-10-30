from rest_framework import serializers

from apps.assignments.models import Question

class QuestionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'title', 'description', 'question_type', 'points', 'is_active']
        read_only_fields = ['id']
        
__all__ = ['QuestionCreateSerializer']