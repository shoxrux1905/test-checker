from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .filters import SubmissionFilter
from .serializers import SubmissionListSerializer
from apps.assignments.models import Submission


class SubmissionListAPIView(generics.ListAPIView):
    serializer_class = SubmissionListSerializer
    queryset = Submission.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_class = SubmissionFilter

    search_fields = ['assigment_title','student__first_name',"student__last_name"]
    ordering_fields = ['submitted_at','total_score','percentage_score']


    def get_queryset(self):
        user=self.request.user

        if user.role=='student':
            return Submission.objects.filter(student=user)
        elif user.role=='teacher':
            return Submission.objects.filter(assignment_teacher=user)
        elif user.role=='admin':
            return Submission.objects.all()
        return Submission.objects.none()


__all__ = ["SubmissionListAPIView"]
