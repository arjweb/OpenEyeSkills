# -*- coding: utf-8 -*-
from django.shortcuts import render


def home(request):
    return render(request, "openeye/index.html", {})


# Render robots.txt and humans.txt if requested
def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")
