from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
from .froms import *

# Create your views here.

class HomeView(View):
    def get(self, request):
        last_news = News.objects.all().order_by('-id')
        random_news = News.objects.all().order_by('?')
        last = News.objects.last()
        reports = Reports.objects.all().order_by('-id')
        context = {
            'last_news':last_news[:4],
            'random_news':random_news[:4],
            'last':last,
            'reports':reports
        }
        return render(request,'index.html', context)


class ReportsView(View):
    def get(self, request):
        reports = Reports.objects.all().order_by('-id')
        context = {
            'reports':reports,
        }
        return render(request, 'classic.html', context)


class NewsView(View):
    def get(self, request):
        news = News.objects.all()
        context = {
            'news':news,
        }
        return render(request, 'news.html', context)


def news_detail(request, pk):
    news = News.objects.get(pk=pk)
    comments = Comments.objects.filter(news=news).order_by('-id')
    context = {
        'news':news,
        'comments':comments
    }
    return render(request,'blog-single.html', context)

def comment(request):
    news_id = request.GET.get('id')
    news = News.objects.get(id=news_id)

    comment = request.GET.get('comment')
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    if comment and name and surname:
        new = Comments.objects.create(
            news=news,
            name=name,
            surname=surname,
            message=comment
        )
        new.save()
        print(new.date.date())
        json = {
            'name':name,
            'surname':surname,
            'comment':comment,
            'date':'hozir',
            'status':'ERROR'
            }
    else:
        json = {'status':'ERROR'}
    return JsonResponse(json)


def report_detail(request, pk):
    repo = Reports.objects.get(pk=pk)
    context = {
        'repo':repo
    }
    return render(request, 'repo-single.html', context)