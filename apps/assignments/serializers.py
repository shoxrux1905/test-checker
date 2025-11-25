from rest_framework import serializers
from apps.assignments.models import Appeal


class AppealSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.get_full_name", read_only=True)
    submission_title = serializers.CharField(
        source="submission.assignment.title", read_only=True
    )
    reviewed_by_name = serializers.CharField(
        source="reviewed_by.get_full_name", read_only=True
    )

from rest_framework import serializers
from apps.assignments.models import Assignment


class AssignmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Assignment
        fields = "__all__"

    def validate(self, data):
        assignment_type = data.get("assignment_type")

        start_time = data.get("start_time")
        end_time = data.get("end_time")
        duration = data.get("duration_minutes")
        due_date = data.get("due_date")

       
        # HOMEWORK RULES
       
        if assignment_type == "homework":
            # Homework shouldn't have exam-only fields
            if start_time or end_time or duration:
                raise serializers.ValidationError(
                    "Homework cannot have start_time, end_time, or duration_minutes."
                )

            # Homework must have due_date
            if not due_date:
                raise serializers.ValidationError(
                    "Homework must include a due_date."
                )

        # EXAM RULES
       
        if assignment_type == "exam":
            # Exams must have start_time, end_time, and duration
            missing = []
            if not start_time:
                missing.append("start_time")
            if not end_time:
                missing.append("end_time")
            if not duration:
                missing.append("duration_minutes")

            if missing:
                raise serializers.ValidationError(
                    f"Exam is missing required fields: {', '.join(missing)}"
                )

            # Exam shouldn't have due_date
            if due_date:
                raise serializers.ValidationError(
                    "Exam should not have a due_date."
                )

            if start_time and end_time and start_time >= end_time:
                raise serializers.ValidationError(
                    "Exam start_time must be before end_time."
                )

        return data


    class Meta:
        model = Appeal
        fields = [
            "id",
            "student",
            "student_name",
            "submission",
            "submission_title",
            "reason",
            "status",
            "reviewed_by",
            "reviewed_by_name",
            "review_notes",
            "reviewed_at",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "student_name",
            "submission_title",
            "reviewed_by_name",
            "created_at",
            "updated_at",
        ]
