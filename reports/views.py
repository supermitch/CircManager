from django.shortcuts import render_to_response
from django.template import RequestContext

from products.models import Product
from subs.models import Subscription

from reports.forms import ProductForm

def upcoming(request):

    if request.method == 'GET':
        form = ProductForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data

            active_products = cd['Product']

            subs = Subscription.objects.filter(product_key=cd['Product'])
            subs = subs.filter(last_issue__lte=cd['Product'].issue_no + 3)

            active_products.subs = subs
        return render_to_response('reports/upcoming.html',
                                 {'form': form,
                                  'products': active_products},
                                  context_instance=RequestContext(request))
    else:
        form = ProductForm()

        #We don't actually have active / inactive products yet!
        #active_products = Products.objects.filter(status__iexact='Active')
        active_products = Product.objects.all()

        for prod in active_products:

            subs = Subscription.objects.filter(product_key=prod)
            subs = subs.filter(last_issue__lte=prod.issue_no + 3)

            prod.subs = subs # Save this products subs. Is there a better way?
       
        return render_to_response('reports/upcoming.html',
                                 {'form': form,
                                  'products': active_products},
                                  context_instance=RequestContext(request))
