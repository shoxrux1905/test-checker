from django.db import models
from django.contrib.auth import get_user_model
from apps.common.models import BaseModel

User = get_user_model()


class Group(BaseModel):
    """Group model for class management"""
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='taught_groups')
    students = models.ManyToManyField(
        User, related_name='enrolled_groups', blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.teacher.get_full_name()}"


class Question(BaseModel):
    QUESTION_TYPES = [
        ('test', 'Test (Multiple Choice)'),
        ('file', 'File Upload'),
        ('text', 'Text Answer'),
        ('code', 'Code Writing'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    points = models.PositiveIntegerField(default=1)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_questions')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} ({self.get_question_type_display()})"


class AnswerOption(BaseModel):
    """Answer options for test questions"""
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='answer_options')
    option_text = models.TextField()
    is_correct = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.question.title} - Option {self.order}"


class StudentAnswer(BaseModel):
    """Student's answer to a question"""
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='student_answers')
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='student_answers')

    selected_option = models.ForeignKey(
        AnswerOption, on_delete=models.CASCADE, blank=True, null=True)

    text_answer = models.TextField(blank=True)

    file_answer = models.FileField(
        upload_to='answers/files/', blank=True, null=True)

    code_answer = models.TextField(blank=True)

    is_correct = models.BooleanField(default=False)
    points_earned = models.PositiveIntegerField(default=0)
    feedback = models.TextField(blank=True)

    class Meta:
        unique_together = ['question', 'student']

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.question.title}"


class Assignment(BaseModel):
    """Assignment model for exams and homework"""
    ASSIGNMENT_TYPES = [
        ('exam', 'Exam'),
        ('homework', 'Homework'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    assignment_type = models.CharField(max_length=10, choices=ASSIGNMENT_TYPES)
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name='assignments')
    questions = models.ManyToManyField(
        Question, related_name='assignments', blank=True)
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='created_assignments')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField(
        help_text="Duration in minutes")

    total_points = models.PositiveIntegerField(default=100)
    passing_score = models.PositiveIntegerField(default=60)
    max_attempts = models.PositiveIntegerField(default=1)
    allow_late_submission = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.group.name}"


class TestSession(BaseModel):
    """Test session model for exam sessions"""
    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='test_sessions')
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='sessions')
    session_token = models.CharField(max_length=100, unique=True)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.assignment.title}"


class Submission(BaseModel):
    """Submission model for student submissions"""
    SUBMISSION_STATUS = [
        ('in_progress', 'In Progress'),
        ('submitted', 'Submitted'),
        ('graded', 'Graded'),
    ]

    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='submissions')
    assignment = models.ForeignKey(
        Assignment, on_delete=models.CASCADE, related_name='submissions')
    test_session = models.ForeignKey(
        TestSession, on_delete=models.CASCADE, related_name='submissions', null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=SUBMISSION_STATUS, default='in_progress')

    started_at = models.DateTimeField(auto_now_add=True)
    submitted_at = models.DateTimeField(blank=True, null=True)
    time_spent_minutes = models.PositiveIntegerField(default=0)

    total_score = models.PositiveIntegerField(default=0)
    percentage_score = models.DecimalField(
        max_digits=5, decimal_places=2, default=0.00)
    is_passed = models.BooleanField(default=False)

    class Meta:
        unique_together = ['student', 'assignment']

    def __str__(self):
        return f"{self.student.get_full_name()} - {self.assignment.title}"

    def save(self, *args, **kwargs):
        if self.assignment.total_points > 0:
            self.percentage_score = (
                self.total_score / self.assignment.total_points) * 100

        self.is_passed = self.percentage_score >= self.assignment.passing_score

        super().save(*args, **kwargs)


class Result(BaseModel):
    """Result model for grading results"""
    submission = models.OneToOneField(
        Submission, on_delete=models.CASCADE, related_name='result')
    graded_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='graded_results')
    final_score = models.PositiveIntegerField()
    feedback = models.TextField()
    is_final = models.BooleanField(default=False)
    graded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Result for {self.submission.student.get_full_name()} - {self.submission.assignment.title}"


class Appeal(BaseModel):
    """Appeal model for grade appeals"""
    APPEAL_STATUS = [
        ('pending', 'Pending'),
        ('under_review', 'Under Review'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]

    student = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='appeals')
    submission = models.ForeignKey(
        Submission, on_delete=models.CASCADE, related_name='appeals')
    reason = models.TextField()
    status = models.CharField(
        max_length=20, choices=APPEAL_STATUS, default='pending')
    reviewed_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='reviewed_appeals')
    review_notes = models.TextField(blank=True)
    reviewed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Appeal by {self.student.get_full_name()} for {self.submission.assignment.title}"
