from django.shortcuts import render
from pagevisits.models import PageVisits
from django.http import HttpResponse


def home_page_view(request):
    html = "index.html"

    PageVisits.objects.create()

    return render(request, html)


def view_page_visits(request):
    v = PageVisits.objects.all()
    print(v)
    return HttpResponse(v)
