from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Cortana, all I need to know is did we lose them?")
