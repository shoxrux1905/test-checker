from django.conf import settings
from django.db import models

from apps.common.models import BaseModel

class Assignment(BaseModel):
    Assignment_type = [
        ('Exam', 'Exam'),
        ('Homework', 'Homework'),
        ('Quiz', 'Quiz'),
    ]
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    assignment_type = models.CharField(max_length=50, choices=Assignment_type, default='Quiz')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
class Question(BaseModel):
    Question_type = [
        ('File', 'File'),
        ('Text', 'Text'),
    ]
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='questions')
    question_file = models.FileField(upload_to='questions/files/', null=True, blank=True)
    question_type = models.CharField(max_length=50, choices=Question_type, default='Text')
    
    def __str__(self):
        return f"Question for {self.assignment.title}"
    
class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_answers')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='answers')
    answer_file = models.FileField(upload_to='answers/files/', null=True, blank=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Answer for {self.question.assignment.title}"
    
class Result(BaseModel):
    grade_choices = [
        ('pass', 'Pass'),
        ('fail', 'Fail'),
    ]
    answer = models.OneToOneField(Answer, on_delete=models.CASCADE, related_name='result')
    score = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    grader = models.CharField(max_length=100)
    grade = models.CharField(max_length=10, choices=grade_choices)
    feedback = models.TextField()
    
    def __str__(self):
        return f"Result for {self.answer.question.assignment.title}"
    
class Appeal(BaseModel):
    appeal_choices = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    result = models.ForeignKey(Result, on_delete=models.CASCADE, related_name='appeals')
    reason = models.CharField(max_length=500)
    status = models.CharField(max_length=10, choices=appeal_choices, default='pending')
    
    def __str__(self):
        return f"Appeal for {self.result.answer.question.assignment.title}"