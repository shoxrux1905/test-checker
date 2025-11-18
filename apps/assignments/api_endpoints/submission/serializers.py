from rest_framework import serializers
from apps.assignments.models import Submission


class SubmissionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)
    assignment_title = serializers.CharField(source="assignment.title", read_only=True)

    class Meta:
        model = Submission
        fields = [
            "id",
            "student",
            "student_name",
            "assignment",
            "assignment_title",
            "test_session",
            "status",
            "started_at",
            "submitted_at",
            "time_spent_minutes",
            "total_score",
            "percentage_score",
            "is_passed",
        ]
        read_only_fields = ["percentage_score", "is_passed", "started_at", "student"]
