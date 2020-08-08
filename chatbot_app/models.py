from django.db import models

# Create your models here.
class Conversation(models.Model):
    query = models.TextField()
    response = models.TextField()
