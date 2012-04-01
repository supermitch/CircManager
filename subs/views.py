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
            q = q.filter(status__iexact='Active')
            q = q.filter(term_length__gt=0)

            u = list(q) # save current records before updating

            # Presently no option for more than 1 issue shipped
            rec_count = q.update(term_length=F('term_length') - 1)

            return render_to_response('subs/shipped.html',{
                'q': q, 'u': u,
                                      'rec_count': rec_count
                                      })
    else:
        form = SendIssueForm()

    return render_to_response('subs/ship_product.html',
                              {'form': form},
                              context_instance=RequestContext(request))


def ship_success(request):
    return render_to_response('subs/shipped.html')
