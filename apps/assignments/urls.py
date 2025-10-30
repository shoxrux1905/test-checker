from django.urls import path

from apps.assignments.api_endpoints import QuestionListAPIView, QuestionCreateAPIView, QuestionUpdateAPIView, QuestionDeleteAPIView

urlpatterns = [
    path('questions_list/', QuestionListAPIView.as_view(), name='questions_list'),
    path('questions_create/', QuestionCreateAPIView.as_view(), name='questions_create'),
    path('questions_update/<int:pk>/', QuestionUpdateAPIView.as_view(), name='questions_update'),
    path('questions_delete/<int:pk>/', QuestionDeleteAPIView.as_view(), name='questions_delete'),
]
