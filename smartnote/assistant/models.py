from django.db import models
from django.contrib.auth.models import User

class Tone(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Summary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    summary_text = models.TextField()
    tone = models.ForeignKey(Tone, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Summary by {self.user.username}"