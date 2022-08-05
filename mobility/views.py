import json

from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.conf import settings

import pandas as pd
import plotly.offline as opy
import plotly.express as px

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
    fips = request.GET.get('fips', None)
    context = {'fips': fips, 'metric': metric}
    # # plotly example
    # if settings.DEBUG:
    #     file_path = ''
    #     url = ''

    # else:
    #     file_path = '/home/upwardmobility/upwardmobility.pythonanywhere.com/'
    #     url = "https://upwardmobility.pythonanywhere.com/compare-counties"
    # f = open(f'{file_path}geojson-counties-fips.json')
    # # returns JSON object as
    # # a dictionary
    # counties = json.load(f)

    # df = pd.read_csv(f"{file_path}counties_merged.csv",
    #                 dtype={"fips": str})[['FIPS', metric, 'NAME']]

    # df['FIPS'] = df['FIPS'].astype(int).astype(str).str.zfill(5)

    # df['LINK'] = "[Link](https://upwardmobility.pythonanywhere.com/compare-counties?fips=" + df['FIPS'] + ")"
    # if metric:
    #     low = min(df[metric].values)
    #     high = max(df[metric].values)
    # else:
    #     low = 0
    #     high = 1
    # fig2 = px.choropleth(df, geojson=counties, locations='FIPS', color=metric,
    #                         color_continuous_scale="Viridis",
    #                         range_color=(low, high),
    #                         scope="usa",
    #                         labels={metric:metric},hover_data=["NAME", metric])



    # fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    # pl_div = opy.plot(fig2, output_type='div', include_plotlyjs=False)

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
