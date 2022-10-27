import csv

from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице
    with open(settings.BUS_STATION_CSV, "r", encoding="UTF-8") as file:
        stat_list = []
        stat_bus = csv.reader(file)
        for st in stat_bus:
            st_dict = {"Name": st[1], "Street": st[4], "District": st[6]}
            stat_list.append(st_dict)
        stat_list.pop(0)
        number_page = int(request.GET.get("page", 1))
        paginator = Paginator(stat_list, 10)
        page = paginator.get_page(number_page)

    context = {
            'bus_stations': page,
            'page': page,
    }
    return render(request, 'stations/index.html', context)
