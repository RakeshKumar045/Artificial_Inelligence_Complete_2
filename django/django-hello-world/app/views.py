# -*- coding: utf-8 -*-
from django.http import HttpResponse


def index(request):
    """
    Function that shows the hello world with an Http Response.
    """
    return HttpResponse("Hello World with Django 2")
