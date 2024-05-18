from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    article_objects = Article.objects.all()
    print(articles_list)
    context = {'object_list':article_objects}
    # print(context)
    return render(request, template, context)
