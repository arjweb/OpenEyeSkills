# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from catalogue.models import TopicArea


def home(request):
    return render(request, "openeye/index.html", {})


# Render robots.txt and humans.txt if requested
def home_files(request, filename):
    return render(request, filename, {}, content_type="text/plain")


# the MAIN PAGE for REGISTERED USERS
class MainView(generic.ListView):

    template_name = "openeye/main.html"
    context_object_name = 'topic_list'

    # TODO Make this only active topic areas?
    def get_queryset(self):
        return TopicArea.objects.all().order_by('name')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MainView, self).dispatch(*args, **kwargs)
