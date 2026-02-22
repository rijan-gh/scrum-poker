from django.db import models
from django.contrib.auth.models import User
from db_models.session import Session

# Task / Story Model
class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('VOTING', 'Voting'),
        ('COMPLETED', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='tasks')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
