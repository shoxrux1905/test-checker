from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from django.shortcuts import get_object_or_404
from apps.assignments.api_endpoints.submission.serializers import SubmissionSerializer
from apps.assignments.models import Submission


class SubmissionDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        submission = get_object_or_404(Submission, pk=pk)

        if not request.user.is_superuser and submission.student != request.user:
            return Response(
                {"detail": "Sizga ruxsat berilmagan!"}, status=status.HTTP_403_FORBIDDEN
            )

        serializer = SubmissionSerializer(submission)
        return Response(serializer.data, status=status.HTTP_200_OK)
