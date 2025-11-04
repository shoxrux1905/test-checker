from rest_framework import generics

from apps.assignments.api_endpoints.QuestionDelete.serializers import QuestionDeleteSerializer
from apps.assignments.models import Question

class QuestionDeleteAPIView(generics.DestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDeleteSerializer

    def perform_destroy(self, instance):
        instance.delete()
