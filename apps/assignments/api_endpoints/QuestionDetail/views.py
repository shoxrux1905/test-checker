from rest_framework import generics

from apps.assignments.api_endpoints.QuestionDetail.serializers import QuestionDetailSerializer
from apps.assignments.models import Question

class QuestionDetailAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer
    
    