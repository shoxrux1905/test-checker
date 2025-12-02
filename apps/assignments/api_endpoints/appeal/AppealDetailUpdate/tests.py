from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient, APITestCase

from apps.users.models import User
from apps.assignments.models import Appeal, Assignment, Group, Submission


class AppealDetailUpdateTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.teacher = User.objects.create_user(role='teacher',
                                                username='teacher',
                                                password='teacher')
        self.admin = User.objects.create_user(role='admin',
                                              username='admin',
                                              password='admin')
        self.student = User.objects.create_user(role='student',
                                                username='student',
                                                password='student')
        self.group = Group.objects.create(name='Test group', teacher=self.teacher)
        self.assignment = Assignment.objects.create(created_by=self.teacher,
                                                    title='Test assignment',
                                                    description='Test description',
                                                    passing_score=80,
                                                    start_time=datetime.now(),
                                                    end_time=datetime.now(),
                                                    duration_minutes=60,
                                                    total_points=100,
                                                    allow_late_submission=False,
                                                    is_active=True,
                                                    group=self.group)
        self.submission = Submission.objects.create(student=self.student, assignment=self.assignment)
        self.appeal = Appeal.objects.create(student=self.student,
                                            submission=self.submission,
                                            reason='Test appeal',
                                            status='pending',
                                            reviewed_by=self.teacher,
                                            review_notes='Test review notes',
                                            reviewed_at=datetime.now())
        self.url = reverse('appeal-detail-update', args=[self.appeal.id])


    def test_appeal_detail(self):
        self.client.force_authenticate(user=self.teacher)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['id'], self.appeal.id)
        self.assertEqual(response.data['student'], self.student.id)
        self.assertEqual(response.data['submission'], self.submission.id)
        self.assertEqual(response.data['reason'], self.appeal.reason)
        self.assertEqual(response.data['status'], self.appeal.status)
        self.assertEqual(response.data['reviewed_by'], self.teacher.id)
        self.assertEqual(response.data['review_notes'], self.appeal.review_notes)


__all__ = ['AppealDetailUpdateTestCase']
