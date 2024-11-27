from django.db import models
from django.contrib.auth import get_user_model


class Todo(models.Model):
    STATUS_CHOICES = (
        ('done', 'done'),
        ('in_progress', 'in_progress'),

    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='in_progress')

    def __str__(self):
        return self.title
