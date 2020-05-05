from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Author(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.user.username


class Blog(models.Model):
	title = models.CharField(max_length=255)
	overview = models.TextField()
	timestamp = models.DateTimeField(auto_now_add = True)
	comments = models.IntegerField(default=0)
	views = models.IntegerField(default=0)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
