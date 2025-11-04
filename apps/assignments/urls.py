from django.urls import path
from apps.assignments.api_endpoints.assignments.views import AssignmentListCreateAPIView, AssignmentDetailAPIView


urlpatterns = [
    path('assignments/', AssignmentListCreateAPIView.as_view(), name='assignment-list-create'),
    path('assignments/<int:pk>/', AssignmentDetailAPIView.as_view(), name='assignment-detail'),

]
