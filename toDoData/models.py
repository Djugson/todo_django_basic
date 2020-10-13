from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDo(models.Model):
	title = models.CharField(max_length=150)
	description = models.TextField(blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	complated_date = models.DateTimeField(null=True, blank=True)
	priority = models.BooleanField(default=False)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
