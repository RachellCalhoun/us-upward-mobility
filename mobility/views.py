from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Hello, world. You're at the mobility index.")


def index(request):
    template = loader.get_template('mobility/index.html')
    context = {
        'filler': 'latest_question_list',
    }
    return HttpResponse(template.render(context, request))
