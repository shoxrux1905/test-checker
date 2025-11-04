from rest_framework import generics

from apps.assignments.api_endpoints.QuestionList.serializers import AssignmentSerializer
from apps.assignments.models import Assignment

class AssignmentListAPIView(generics.ListAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
