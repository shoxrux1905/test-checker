from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from apps.assignments.models import Submission
from .serializers import SubmissionSerializer


class SubmissionListCreateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):

        if request.user.is_staff:
            submissions = Submission.objects.all()
        else:
            submissions = Submission.objects.filter(student=request.user)
        serializer = SubmissionSerializer(submissions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):

        data = request.data.copy()
        data['student'] = request.user.id
        serializer = SubmissionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
