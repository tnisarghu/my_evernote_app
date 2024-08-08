from django.db import models
from notes.models import Note

class SearchIndex(models.Model):
    note = models.OneToOneField(Note, on_delete=models.CASCADE)
    title_index = models.CharField(max_length=200, db_index=True)
    content_index = models.TextField(db_index=True)

    def save(self, *args, **kwargs):
        self.title_index = self.note.title
        self.content_index = self.note.content
        super().save(*args, **kwargs)