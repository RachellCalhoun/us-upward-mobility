from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


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
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))


class PostListView(ListView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class PostDetailView(DetailView):
    # specify the model to use
    model = Post
