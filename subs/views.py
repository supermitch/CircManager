from django.shortcuts import render_to_response
from django.template import RequestContext

from subs.forms import SubscribeForm

from subs.models import Subscription
from products.models import SaleItem

def subscribe(request):

    if request.method == 'POST':
        
        form = SubscribeForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data

            prod = cd['sale_item'].product

            subscription = Subscription(
                payee_key = cd['subscriber'],
                product_key = prod,
                first_issue = prod.issue_no,
                last_issue = prod.issue_no + cd['sale_item'].term,
                status = 'Active',
                gift_bool = cd['gift_bool'],
                gift_name = cd['gift_name'],
                gift_msg = cd['gift_msg'])

            subscription.save()

            return render_to_response('subs/subscribe.html',{
                                      'success': True,
                                      'subscription': subscription
                                      })

    else:
        form = SubscribeForm()
    return render_to_response('subs/subscribe.html',
                              {'form': form},
                              context_instance=RequestContext(request))
