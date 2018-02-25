# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Article
# Create your views here.
def home(request):
	post_list = Article.objects.order_by('-date_time')
	return render(request, 'article/home.html', {'post_list': post_list})

def detail(request, post_id):
	post = get_object_or_404(Article, id=post_id)
	return render(request, 'article/post.html', {'post':post})
