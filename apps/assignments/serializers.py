from rest_framework import serializers
from apps.assignments.models import Appeal

class AppealSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.get_full_name', read_only=True)
    submission_title = serializers.CharField(source='submission.assignment.title', read_only=True)
    reviewed_by_name = serializers.CharField(source='reviewed_by.get_full_name', read_only=True)

    class Meta:
        model = Appeal
        fields = [
            'id',
            'student',
            'student_name',
            'submission',
            'submission_title',
            'reason',
            'status',
            'reviewed_by',
            'reviewed_by_name',
            'review_notes',
            'reviewed_at',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['student_name', 'submission_title', 'reviewed_by_name', 'created_at', 'updated_at']
