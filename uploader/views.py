from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template import Context # useless?
from django.http import HttpResponse
from django.core.context_processors import csrf # security thing
from django.template import RequestContext

from models import UploadFileForm # import our upload form model


#def index(request):
#    context = {}
#    context.update(csrf(request))  
#    return render_to_response('uploader/index.html', context)

def success(request):
    context = {}
    context.update(csrf(request))  
    return render_to_response('uploader/success.html', context)

def upload_file(request):
    context = {}                    # Not necessary?
    context.update(csrf(request))   # Not necessary?

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('../success')
            
    else:
        form = UploadFileForm()
    return render_to_response('uploader/index.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    destination = open('c:/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    


