from django.db import models
from django.contrib.auth.models import User


# 1️⃣ Session Model
class Session(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_sessions')
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    participants = models.ManyToManyField(
        User,
        through='SessionParticipant',
        related_name='sessions_joined'
    )

    def __str__(self):
        return self.name