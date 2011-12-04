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
            return HttpResponseRedirect('../success')
            # return render_to_response('uploader/results.html', name_list, context_instance=RequestContext(request))
            
    else:
        form = UploadFileForm()
    return render_to_response('uploader/index.html', {'form': form}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
    import os.path      # Added so I could do away with absolute path to templates, see below
    import csv          # Let's read our CSV file the proper way using python 
    
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
    # infile = open(infile, 'r')    # open the .csv file for reading

    # except IOError as e:    # if file open failed for whatever reason

#    for line in infile:     # for each line in the infile list
#       fields = line.split(',')
#        c = Customer(first_name=fields[1], last_name=fields[2], other_name=fields[3], company=fields[4], birthday="2001-02-12")
#       c.save()

    with open(infile, 'U') as csvFile:

        csvSample = csvFile.read(1024)     # Read a sample of the file for our csv sniffers
        csvFile.seek(0)                             # rewind the file

        dialect = csv.Sniffer().sniff(csvSample)    # figure out the dialect, according to the sniffer    

        inReader = csv.reader(csvFile, dialect)     # Read our .csv file

        # This next line fails because of newline characters in the file.
        # I cannot figure out how to handle them properly!
        # if csv.Sniffer().has_header(csvSample.strip()):     # if we have headers in our file (according to the sniffer)
        inReader.next()                         # skip a row. I think we can use dictReader for this, would be better?

        for row in inReader:
            #c = Customer(first_name=fields[1], last_name=fields[2], other_name=fields[3], company=fields[4], birthday="2001-02-12")
            c = Customer(
                # Personal details
                #greeting=row[0],   # don't have this in the model yet... todo
                first_name=row[1], last_name=row[2], other_name=row[3]
                , company=row[4], birthday="2011-12-12" # =row[5] Need valid date format.
                , phone="6041234567", email=row[7]
                # Billing address:
                , bill_add_1=row[8], bill_add_2=row[9], bill_city=row[10]
                , bill_province=row[11], bill_postal=row[12], bill_country=row[13]
                # Shipping address:
                , ship_as_bill=row[14]
                , ship_add_1=row[15], ship_add_2=row[16], ship_city=row[17]
                , ship_province=row[18], ship_postal=row[19], ship_country=row[20]
                )
            c.save()

    # infile.close()  # Close the csv input file # Automagically close a file with 'with'

    


