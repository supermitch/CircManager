from django.shortcuts import render_to_response

from products.models import Product
from subs.models import Subscription


def upcoming(request):

    #We don't actually have active / inactive products yet!
    #active_products = Products.objects.filter(status__iexact='Active')
    active_products = Product.objects.all()

    for prod in active_products:

        subs = Subscription.objects.filter(product_key= prod)
        subs = subs.filter(last_issue__lte=prod.issue_no + 3)

        prod.subs = subs # Save this products subs. Is there a better way?
   
    return render_to_response('reports/upcoming.html',
                             {'products': active_products})
