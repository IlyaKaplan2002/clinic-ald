from django.db import models

class CommentModel(models.Model):
	name = models.CharField(max_length=30)
	content = models.TextField(max_length=5000)