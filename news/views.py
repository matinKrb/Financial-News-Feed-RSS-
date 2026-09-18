from django.shortcuts import render , get_object_or_404
from django.core.paginator import Paginator
import feedparser
from . import models
from datetime import datetime



# Create your views here.

def index(request):
    f = request.GET.get('category')
    if f:
        q = models.Category.objects.get(slug=f)
        news_list = q.news.all()
        selectedCategory = q
        newsSourse = q.news_source.all()
    else:
        news_list = models.News.objects.all()
        selectedCategory = None
        newsSourse = models.NewsSource.objects.all()

    paginator = Paginator(news_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    page_range = paginator.get_elided_page_range(page_obj.number, on_each_side=1, on_ends=1)

    context = {
        'news': page_obj,
        'page_range': page_range,
        'newsSourse': newsSourse,
        'category': models.Category.objects.all(),
        'selectedCategory': selectedCategory,
    }
    return render(request , 'home.html' , context)

def detail(request, pk):
    q = models.News.objects.get(pk=pk)
    newscategory = q.category
    relatednews = newscategory.news.all()[:5]
    context = {
        'news' : q,
        'category' : models.Category.objects.all(),
        'relatedNews' : relatednews,
    }
    return render(request , 'detail.html' , context)