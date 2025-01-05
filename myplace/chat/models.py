from django.db import models

# Create your models here.
from django.db import models

class ChatLog(models.Model):
    user_input = models.TextField()
    gpt_response = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat at {self.created_at}"
