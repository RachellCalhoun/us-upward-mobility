from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import pandas as pd
import plotly.offline as opy
from urllib.request import urlopen
import json
import plotly.express as px

from mobility.models import Post
# def index(request):
#     return HttpResponse("Hello, world. You're at the mobility index.")


def index(request):
    template = loader.get_template('mobility/index.html')
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))

def compare_counties(request):
    template = loader.get_template('mobility/compare_counties.html')
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))


def national_view(request):
    template = loader.get_template('mobility/national_view.html')
    # plotly example
    f = open('geojson-counties-fips.json')
    # returns JSON object as
    # a dictionary
    counties = json.load(f)

    df = pd.read_csv("counties_merged.csv",
                    dtype={"fips": str})

    fig2 = px.choropleth(df, geojson=counties, locations='FIPS', color='proportion_homeless',
                            color_continuous_scale="Viridis",
                            range_color=(0, 1),
                            scope="usa",
                            labels={'proportion_homeless':'proportion_homeless'}
                                )
    print('fig done')
    fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    print('fig update done')
    pl_div = opy.plot(fig2, output_type='div', include_plotlyjs=False)
    print('create plt')
    context = { 'pl_div': pl_div}
    return HttpResponse(template.render(context, request))

class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    # specify the model to use
    model = Post
