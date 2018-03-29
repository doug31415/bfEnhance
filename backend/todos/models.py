from django.db import models

# Create your models here.

class Todo(models.Model):
  """
  Model representing an author.
  """
  is_complete = models.BooleanField(default=False)
  name = models.CharField(max_length=100)

  class Meta:
    ordering = ["name", "is_complete"]
