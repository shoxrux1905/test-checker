from rest_framework import serializers
from apps.assignments.models import Question

class QuestionDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
