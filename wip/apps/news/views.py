from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import News
from .forms import NewsForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

number_of_news = 10                                                         #default number of news on page#


def news_feed(request):
    global number_of_news
    if request.method == 'POST' and request.POST.get('news_title'):         #check if there are news to add#
        news_title = request.POST['news_title']
        news_text = request.POST['news_text']
        if request.FILES.get('news_image'):
            news_image = request.FILES['news_image']
        else:
            news_image = request.POST['news_image']
        ins = News(news_title=news_title, news_text=news_text, news_image=news_image)
        ins.save()                                                          #save to database#
    elif request.method == 'POST' and request.POST.get('number_of_news'):   #check if number of news on page was changed#
        number_of_news = request.POST['number_of_news']
    page_number = request.GET.get('page', 1)
    news_list = News.objects.order_by('-date')
    news_lists = Paginator(news_list, number_of_news)
    page = news_lists.get_page(page_number)
    return render(request, "news/news.html", context={'news_list': page})   #render page with news feed#


def create(request):                                                        #function to show page with news forms#
    form = NewsForm()
    data = {'form': form}
    return render(request, "news/create.html", data)
