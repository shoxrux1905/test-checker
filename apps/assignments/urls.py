from django.urls import path

from apps.assignments.api_endpoints.submission.views.submission_create_view import SubmissionCreateAPIView
from apps.assignments.api_endpoints.submission.views.submission_detail_view import SubmissionDetailAPIView
from apps.assignments.api_endpoints.assignments.views import AssignmentListCreateAPIView, AssignmentDetailAPIView


urlpatterns = [
    path('create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('<int:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),
    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
]
