from django.shortcuts import render, get_object_or_404
from .models import Article
from django.utils import timezone

def article_list(request):
	posts = Article.objects.filter(article_date__lte=timezone.now()).order_by('article_date')
	return render(request, 'article/post_list.html', {'posts': posts})

def article_detail(request, pk):
	post = get_object_or_404(Article, pk=pk)
	return render(request, 'article/post_detail.html', {'post': post})