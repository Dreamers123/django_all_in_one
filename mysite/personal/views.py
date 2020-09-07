from django.shortcuts import render
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_blog_queryset
from blog.models import BlogPost
from personal.models import Question
# def home_screen_view(request):
#
#     context={}
#     # list_of_values = ['physics', 'chemistry', 1997, 2000];
#     # context['list']=list_of_values
#     questions=Question.objects.all()
#     context['list']=questions
#     return render(request,"personal/home.html",context)

def home_screen_view(request, *args, **kwargs):

	context = {}

	# Search
	query = ""
	if request.GET:
		query = request.GET.get('q', '')
		context['query'] = str(query)

	blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)



	# Pagination
	# page = request.GET.get('page', 1)
	# # blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
	# try:
	# 	# blog_posts = blog_posts_paginator.page(page)
	# except PageNotAnInteger:
	# 	blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
	# except EmptyPage:
	# 	blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

	context['blog_posts'] = blog_posts

	return render(request, "personal/home.html", context)

def ping_pong(request):
    return render(request,"personal/pin_pong.html",{})

def chart_view(request):
    return render(request,"personal/chart.html",{})