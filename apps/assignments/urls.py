from django.urls import path
from apps.assignments.api_endpoints.submission.views import SubmissionListCreateAPIView

urlpatterns = [
    path('submissions/', SubmissionListCreateAPIView.as_view(), name='submission-list-create'),
]
