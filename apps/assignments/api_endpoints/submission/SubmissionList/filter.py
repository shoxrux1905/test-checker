
import django_filters
from apps.assignments.models import Submission


class SubmissionFilter(django_filters.FilterSet):
    assignment_title=django_filters.CharFilter(field_name="assignment_title",lookup_expr="icontains")
    status=django_filters.CharFilter(lookup_expr="iexact")
    submitted_after=django_filters.DateTimeFilter(field_name="submitted_at",lookup_expr='gte')
    submitted_before=django_filters.DateTimeFilter(field_name="submitted_at",lookup_expr='lte')
    student_name=django_filters.CharFilter(field_name="student__first_name",lookup_expr='icontains')
    
    
    class Meta:
        model=Submission
        fields=['status','assignment_title','student_name','submitted_after','submitted_before']