from django.urls import path

from apps.assignments.api_endpoints import QuestionDetailAPIView, QuestionUpdateAPIView
from apps.assignments.api_endpoints import QuestionCreateAPIView, QuestionDeleteAPIView
from apps.assignments.api_endpoints import AssignmentListAPIView


urlpatterns = [
    path('questions_detail/', QuestionDetailAPIView.as_view(), name='questions_detail'),
    path('questions_create/', QuestionCreateAPIView.as_view(), name='questions_create'),
    path('questions_update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='questions_update'),
    path('questions_delete/<int:pk>/', QuestionDeleteAPIView.as_view(), name='questions_delete'),
    
    path('assignments/<int:assignment_id>/questions/', AssignmentListAPIView.as_view(), name='assignment-question-list'),
]
