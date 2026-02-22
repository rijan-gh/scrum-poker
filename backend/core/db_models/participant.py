from django.db import models
from django.contrib.auth.models import User
from db_models.session import Session

# SessionParticipant Model (Many-to-Many Bridge)
class SessionParticipant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'session')

    def __str__(self):
        return f"{self.user.username} in {self.session.name}"