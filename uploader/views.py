from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import RequestContext

from models import UploadFileForm # import our upload form model

from subs.models import Customer


def success(request):
    return render_to_response('uploader/success.html')

def upload_file(request):

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            # name_list = handle_uploaded_file(request.FILES['file']) # return a response from this page
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('../success')
            return render_to_response('uploader/results.html', name_list, context_instance=RequestContext(request))
            
    else:
        form = UploadFileForm()
    return render_to_response('uploader/index.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    import os.path   # Added so I could do away with absolute path to templates, see below
    
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    infile = os.path.join(SITE_ROOT, '../data/upload.txt')

    # See os.path import, above:
    destination = open(infile, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    # return {'name_list': ['mitch', 'ross', 'test']} # holy shit this worked.

    # Try to open the file, catch the exception if it fails?
    # try:
    infile = open(infile, 'r')    # open the .csv file for reading

    # except IOError as e:    # if file open failed for whatever reason

    for line in infile:     # for each line in the infile list
        fields = line.split(',')
        c = Customer(first_name=fields[1], last_name=fields[2], other_name=fields[3], company=fields[4], birthday="2001-02-12")
        c.save()


    infile.close()  # Close the csv input file

    


