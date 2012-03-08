# Create your views here.

from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext


def index(request):
    return render_to_response('index/index.html')
