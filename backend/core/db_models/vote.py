from django.db import models
from django.contrib.auth.models import User
from db_models.task import Task

# Vote Model
class Vote(models.Model):
    FIBONACCI_CHOICES = [
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (5, '5'),
        (8, '8'),
        (13, '13'),
        (21, '21'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='votes')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='votes')
    value = models.IntegerField(choices=FIBONACCI_CHOICES)
    voted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'task')  # One vote per user per task

    def __str__(self):
        return f"{self.user.username} voted {self.value} on {self.task.title}"