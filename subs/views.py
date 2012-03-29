from django.shortcuts import render_to_response
from django.template import RequestContext

# Enable field lookups in queries
from django.db.models import F

from CircManager.subs.forms import SendIssueForm
from subs.models import Subscription

def index(request):
    return render_to_response('subs/index.html',)


def ship_product(request):

    if request.method == 'POST':
        form = SendIssueForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            q = Subscription.objects.filter(
                product_key__exact=cd['product'])
            #q = q.filter(status__iexact="Active") # TODO: implement
            q = q.filter(term_length__gt=0)

            
            # TODO: Verify each subscription has enough issues
            #       remaining to actually decrement.
            # Decrement our terms remaining:
            q.update(term_length=F('term_length') - cd['no_shipped'])

            # Update seems to be happening BEFORE our filter is being
            # applied, so we're not seeing issues that HAD 1 term, if
            # they go to 0! Need to read up on "when filter and update
            # statements get evaluated". We may have to cycle through
            # all our records 1 by 1 anyway, to ensure we don't go to
            # less than 0 terms remaining if they ship > 2 issues!
            return render_to_response('subs/shipped.html', {'q': q})
    else:
        form = SendIssueForm()
    return render_to_response('subs/ship_product.html', {'form': form}, context_instance=RequestContext(request))


def ship_success(request):
    return render_to_response('subs/shipped.html')
