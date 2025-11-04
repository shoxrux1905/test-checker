from django.urls import path
from apps.assignments.api_endpoints.assignments_serializers.views import AssignmentListCreateAPIView, AssignmentDetailAPIView
from apps.assignments.api_endpoints.submissions_serializers.views import SubmissionListCreateAPIView, SubmissionDetailAPIView

urlpatterns = [
    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
    path('submissions/', SubmissionListCreateAPIView.as_view(), name='submission-list-create'),
    path('submissions/<int:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),
]
