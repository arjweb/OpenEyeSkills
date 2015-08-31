from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from .models import TopicArea, CatalogueItem
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ContributeForm
# Create your views here.


# the MAIN PAGE for REGISTERED USERS
class TopicView(generic.ListView):

    template_name = "openeye/topic.html"
    context_object_name = 'resource_list'
    paginate_by = 5

    # TODO Make this only active topic areas?
    def get_queryset(self, *args, **kwargs):
        return CatalogueItem.objects.filter(topic_area_id=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(TopicView, self).get_context_data(**kwargs)
        # context['TopicName'] = TopicArea.objects.filter(id=self.kwargs['pk'])
        context['TopicName'] = TopicArea.objects.get(id=self.kwargs['pk'])
        return context

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(TopicView, self).dispatch(*args, **kwargs)


class DetailView(generic.DetailView):

    template_name = "openeye/resource_detail.html"
    model = CatalogueItem
    context_object_name = 'resource'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(DetailView, self).dispatch(*args, **kwargs)


class ContributeView(generic.CreateView):

    template_name = "openeye/contribute.html"
    form_class = ContributeForm
    success_url = reverse_lazy('MainView')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContributeView, self).dispatch(*args, **kwargs)


