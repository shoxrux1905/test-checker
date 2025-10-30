from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from apps.assignments.api_endpoints.QuestionDelete.serializers import QuestionSerializer
from apps.assignments.models import Question

class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def perform_destroy(self, instance):
        instance.delete()
