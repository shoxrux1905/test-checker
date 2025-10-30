from rest_framework import serializers

from apps.assignments.models import Question

class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['title', 'description', 'question_type', 'points', 'is_active']
        