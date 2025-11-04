from django.urls import path
from apps.assignments.api_endpoints.submission.views.submission_create_view import SubmissionCreateAPIView
from apps.assignments.api_endpoints.submission.views.submission_detail_view import SubmissionDetailAPIView

urlpatterns = [
    path('submissions/create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('submissions/<int:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),
]
