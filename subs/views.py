from django.shortcuts import render_to_response
from django.template import RequestContext
from CircManager.subs.forms import SendIssueForm

def index(request):
    return render_to_response('subs/index.html',)

def ship_product(request):

    if request.method == 'POST':
        form = SendIssueForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                cd['subject'],
                cd['message'],
                cd.get('email', 'noreply@example.com'),
                ['siteowner@example.com'],
            )
            return HttpResponseRedirect('/admin/shipped/')
    else:
        form = SendIssueForm()
    return render_to_response('subs/ship_product.html', {'form': form}, context_instance=RequestContext(request))

    
