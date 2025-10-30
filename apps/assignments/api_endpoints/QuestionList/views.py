from rest_framework import generics

from apps.assignments.api_endpoints.QuestionList.serializers import QuestionListSerializer
from apps.assignments.models import Question

class QuestionListAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionListSerializer
    
    