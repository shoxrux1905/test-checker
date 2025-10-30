from rest_framework import generics


from apps.assignments.api_endpoints.QuestionCreate.serializers import QuestionCreateSerializer
from apps.assignments.models import Question

class QuestionCreateAPIView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionCreateSerializer
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)