from rest_framework import generics,permissions,filters
from apps.assignments.api_endpoints.submission.SubmissionList.filter import SubmissionFilter
from apps.assignments.api_endpoints.submission.SubmissionList.serializers import SubmissionListSerializer
from apps.assignments.models import Submission
from django_filters.rest_framework import DjangoFilterBackend


class SubmissionListView(generics.ListAPIView):
    serializer_class=SubmissionListSerializer
    permission_classes=[permissions.IsAuthenticated]
    queryset=Submission.objects.all()
    
    #filter backends
    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_class=SubmissionFilter
    
    #search and ordering fields
    search_fields=['assigment_title','student__first_name',"student__last_name"]
    ordering_fields=['submitted_at','total_score','percentage_score']
    
    
    def get_queryset(self):
        user=self.request.user
        
        if user.role=='student':
            return Submission.objects.filter(student=user)
        elif user.role=='teacher':
            return Submission.objects.filter(assignment_teacher=user)
        elif user.role=='admin':
            return Submission.objects.all()
        return Submission.objects.none()