from django.shortcuts import render, redirect
from phones.models import Phone

def index(request):
    return redirect('catalog')


def show_catalog(request):
    p = request.GET.get('sort')
    if p == 'name':
        phones = Phone.objects.order_by('name')
    elif p == 'min_price':
        phones = Phone.objects.order_by('price')
    elif p == 'max_price':
        phones = Phone.objects.order_by('-price')
    else: 
        phones = Phone.objects.all()

    template = 'catalog.html'
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    phone = Phone.objects.get(slug = slug)
    template = 'product.html'
    context = {'phone': phone}
    return render(request, template, context)
