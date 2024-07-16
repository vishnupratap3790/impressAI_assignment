from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    text = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    
    def __str__(self):
        return self.text

class UserResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.is_correct = self.answer.strip().lower() == self.question.correct_answer.strip().lower()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.user.username} - {self.question.text}: {self.answer}"
