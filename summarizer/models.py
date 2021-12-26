from django.db import models
from django.utils import timezone
class SavedData(models.Model):
    article = models.TextField()
    summary = models.TextField()
    date_saved = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.article

