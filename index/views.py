from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request):
    # We need to add our request context in order to access
    # session variables in our templates
    #return render_to_response('index/index.html')
    return render_to_response('index/index.html',
        context_instance=RequestContext(request,))

