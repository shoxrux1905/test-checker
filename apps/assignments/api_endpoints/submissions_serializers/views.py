from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.assignments.models import Submission
from .serializers import  SubmissionSerializer
from django.shortcuts import get_object_or_404

class SubmissionListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        if user.is_admin or user.is_teacher:
            submissions = Submission.objects.all()
        else:
            submissions = Submission.objects.filter(student=user)

        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data)

    def post(self, request):
        if not request.user.is_student:
            return Response({'detail': 'Student'}, status=status.HTTP_403_FORBIDDEN)

        serializer = SubmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(student=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SubmissionDetailAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk, user):
        if user.is_admin or user.is_teacher:
            return get_object_or_404(Submission, pk=pk)
        return get_object_or_404(Submission, pk=pk, student=user)

    def get(self, request, pk):
        submission = self.get_object(pk, request.user)
        serializer = SubmissionSerializer(submission)
        return Response(serializer.data)