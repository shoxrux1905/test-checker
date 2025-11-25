from django.urls import path

from apps.assignments.api_endpoints.appeal import\
    AppealListCreateView, AppealDetailUpdateView
from apps.assignments.api_endpoints.submission import\
    SubmissionCreateAPIView, SubmissionDetailAPIView, SubmissionListAPIView
from apps.assignments.api_endpoints.assignment import\
    AssignmentListCreateAPIView, AssignmentDetailAPIView


urlpatterns = [
    path("create/", SubmissionCreateAPIView.as_view(), name="submission-create"),
    path("<int:pk>/", SubmissionDetailAPIView.as_view(), name="submission-detail"),
    path(
        "assignments/",
        AssignmentListCreateAPIView.as_view(),
        name="assignment-list-create",
    ),
    path(
        "assignments/<int:pk>/",
        AssignmentDetailAPIView.as_view(),
        name="assignment-detail",
    ),
    path("appeals/", AppealListCreateView.as_view(), name="appeal-list-create"),
    path(
        "appeals/<int:pk>/",
        AppealDetailUpdateView.as_view(),
        name="appeal-detail-update",
    ),
    path("submissions/create/", SubmissionCreateAPIView.as_view(), name="submission-create"),
    path("submissions/", SubmissionListAPIView.as_view(), name="submission-list-create"),
]
