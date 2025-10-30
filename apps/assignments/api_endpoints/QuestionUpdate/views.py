from rest_framework import generics

from apps.assignments.api_endpoints.QuestionUpdate.serializers import QuestionUpdateSerializer
from apps.assignments.models import Question

class QuestionUpdateAPIView(generics.UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionUpdateSerializer
        
    def perform_update(self, serializer):
        serializer.save()