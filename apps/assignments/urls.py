# from django.urls import path

# from apps.assignments.api_endpoints.submission.views.submission_create_view import SubmissionCreateAPIView
# from apps.assignments.api_endpoints.submission.views.submission_detail_view import SubmissionDetailAPIView
# from apps.assignments.api_endpoints.assignments.views import AssignmentListCreateAPIView, AssignmentDetailAPIView


# urlpatterns = [
#     path('create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
#     path('<int:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),
#     path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
#     path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
# ]
from django.urls import path
from apps.assignments.api_endpoints.submission.views.submission_create_view import SubmissionCreateAPIView
from apps.assignments.api_endpoints.submission.views.submission_detail_view import SubmissionDetailAPIView
from apps.assignments.api_endpoints.assignments.views import AssignmentListCreateAPIView, AssignmentDetailAPIView
from apps.assignments.views import AppealListCreateView, AppealDetailUpdateView

urlpatterns = [
    path('create/', SubmissionCreateAPIView.as_view(), name='submission-create'),
    path('<int:pk>/', SubmissionDetailAPIView.as_view(), name='submission-detail'),

    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),
    path('appeals/', AppealListCreateView.as_view(), name='appeal-list-create'),
    path('appeals/<int:pk>/', AppealDetailUpdateView.as_view(), name='appeal-detail-update'),
]
