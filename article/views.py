# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from .models import Article
# Create your views here.
def home(request):
	blog_list = Article.objects.all()
	return render(request, 'article/home.html', {'blog_list': blog_list})
def detail(request, my_args):
	post = Article.objects.get(id=my_args)
	message = ("title = %s, category = %s, date_time =%s, content = %s") % (post.title, post.category, post.date_time, post.content)
	return HttpResponse(message)

def test(request):
	return render(request, 'article/test.html', {'current_time':datetime.now()})