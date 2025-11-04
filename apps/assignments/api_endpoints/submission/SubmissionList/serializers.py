from pyexpat import model
from rest_framework import serializers
from apps.assignments.models import Submission


class SubmissionListSerializer(serializers.ModelSerializer):
    student_name=serializers.SerializerMethodField()
    assignment_title=serializers.CharField(source="assigment.title",read_only=True)
    
    class Meta:
        model=Submission
        fields=[
            'id','student_name','assigment_title','status',
            'total_score','percentage_score','is_passed','submitted_at',' time_spent_minutes'
        ]
        
    def get_student_name(self,obj):
        return obj.student.get_full_name()