from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "article"
	article_autor = models.ForeignKey('auth.User')
	article_title = models.CharField(max_length = 200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=0)
	def publish(self):
		self.article_date = timezone.now()
		self.save()
	def __str__(self):
		return self.article_title

class Comments(models.Model):
	class Meta():
		db_table = 'comments'
	comments_text = models.TextField()
	comments_article = models.ForeignKey(Article)
