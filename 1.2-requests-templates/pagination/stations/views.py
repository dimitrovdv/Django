import urllib
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import csv
from pagination import settings


def function_csv2():
    content = list()
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content2 = list()
            content2.append(row['Name'])
            content2.append(row['Street'])
            content2.append(row['District'])
            content.append(content2)

    return content

content = function_csv2()

def function_csv():
    cont = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            content = {}
            content['Name'] = row['Name']
            content['Street'] = row['Street']
            content['District'] = row['District']
            cont.append(content)
    return cont

def index(request):
    return redirect(reverse(bus_stations))

def bus_stations(request):
    current_page = 1
    next_page_url = 'next'
    content = function_csv()
    page_number = int(request.GET.get('page',1))
    url = reverse('bus_stations')

    paginator = Paginator(content, settings.ITEMS_PER_PAGE)
    page_obj = paginator.get_page(page_number)
    last_page = paginator.num_pages
    if page_obj.number != last_page:
        if page_obj.has_next():
            params = urllib.parse.urlencode({'page': page_obj.next_page_number()})
            next_page_url = f'{url}?{params}'
        else:
            next_page_url = None
    else:
        next_page_url = None
    if page_obj.has_previous():
        params2 = urllib.parse.urlencode({'page': page_obj.previous_page_number()})
        current_page = page_obj.number
        prev_page_url = f'{url}?{params2}'
    else:
        prev_page_url = None
    last_page = paginator.num_pages
    return render(request, 'stations/index.html', context={
            'bus_stations': page_obj.object_list,
            'current_page': current_page,
            'prev_page_url': prev_page_url,
            'next_page_url': next_page_url,
            'last_page': last_page,
        })


