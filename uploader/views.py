from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from models import UploadFileForm # import our upload form model


def success(request):
    return render_to_response('uploader/success.html')

def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            name_list = handle_uploaded_file(request.FILES['file']) # return a response from this page
            #return HttpResponseRedirect('../success')
            return render_to_response('uploader/results.html', name_list, context_instance=RequestContext(request))
            
    else:
        form = UploadFileForm()
    return render_to_response('uploader/index.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    destination = open('c:/name.txt', 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return {'name_list': ['mitch', 'ross', 'test']} # holy shit this worked.
    
    
    


