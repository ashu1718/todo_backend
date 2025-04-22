import uuid
from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('success', 'Success'),
        ('failure', 'Failure'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def check_status(self):
        now = timezone.now()
        if self.status == 'ongoing' and now > self.deadline:
            self.status = 'failure'
            self.save()
