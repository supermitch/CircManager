from products.models import Product
from subs.models import Subscription


def upcoming(request):

    #We don't actually have active / inactive products yet!
    #active_products = Products.objects.filter(status__iexact='Active')
    active_products = Products.objects.all()

    for prod in active_products:

        print(prod.issue_no)

        subs = Subscription.objects.filter(product_key = prod)
        subs = subs.filter(last_issue__lte=prod.issue_no + 3)

        print(subs)
    
    # Get each product that is active

        # get current issue number

        # get subscriptions for that product that are < 3 terms away

            # send those results to a view
