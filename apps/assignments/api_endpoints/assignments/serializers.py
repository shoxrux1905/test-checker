from rest_framework import serializers
from apps.assignments.models import Assignment

class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = '__all__'

__all__="AssignmentSerializer"