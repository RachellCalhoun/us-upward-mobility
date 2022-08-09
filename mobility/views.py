import json


from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from mobility.models import Post
from mobility.forms import MetricForm, CountyForm

def index(request):
    template = loader.get_template('mobility/index.html')
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

def county_details(request):
    fips = request.GET.get('fips', None)
    form = CountyForm(initial={'fips': request.GET.get('fips', None)})
    context = {'fips': fips, 'form': form}
    template = loader.get_template('mobility/county_details.html')
    return HttpResponse(template.render(context, request))


def national_view(request):
    metric = request.GET.get('metric', 'population')
    metric_form = MetricForm(initial={'metric': request.GET.get('metric', 'population')})
    template = loader.get_template('mobility/national_view.html')

    context = { 'form': metric_form, 'metric': metric}
    return HttpResponse(template.render(context, request))

class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    # specify the model to use
    model = Post
