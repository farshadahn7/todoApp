from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django.shortcuts import reverse


class Todo(models.Model):
    STATUS_CHOICES = (
        ('in_progress', 'in_progress'),
        ('done', 'done'),

    )
    title = models.CharField(max_length=100)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='user')
    slug = models.SlugField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=13, choices=STATUS_CHOICES, default='in_progress')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title+str(self.user.pk))
        return super().save(*args, **kwargs)

    def get_absolute_api_url(self):
        return reverse('todo:api-v1:api_todo-detail', kwargs={'slug': self.slug})
