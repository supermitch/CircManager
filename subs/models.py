from django.db import models
from django.forms import ModelForm

from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):

    GREETINGS = (
        ('Mr.',     'Mr.'),
        ('Mrs.',    'Mrs.'),
        ('Ms.',     'Ms.'),
        ('Dr.',     'Dr.'),
        ('Prof.',   'Prof.'),
        ('Sir',     'Sir'),        
    )
    
    user = models.OneToOneField(User)

    # Customer personal details
    greeting = models.CharField('Greeting',
                                max_length=5,
                                choices=GREETINGS,
                                blank=True)

    # These currently exist in Django "user" module
    #first_name = models.CharField('First Name', max_length=50)
    #last_name = models.CharField('Last Name', max_length=50)
    #email = models.EmailField(blank=True)
    
    other_name = models.CharField('Other Names', max_length=100,blank=True)
    company = models.CharField('Company', max_length=100, blank=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    
    #TODO: we want only 0-9, '-', ' ', '.', 'x', 'ext', and '()' for phone. 
    # Use a validator!
    #from django.core.validators import RegexValidator 
    #import re 
    #phone_regex = re.compile(r'[^A-Za-z0-9 _.-()]+$') # Needs work
    #phone = models.CharField(max_length = 20, unique =False, blank=True, validators=[RegexValidator(regex=phone_regex)] ) 

    phone = models.CharField('Phone number', max_length=50, blank=True)

    # Billing information
    bill_add_1 = models.CharField(max_length=200, blank=True)
    bill_add_2 = models.CharField(max_length=200, blank=True)
    bill_city = models.CharField(max_length=200, blank=True)
    bill_province = models.CharField(max_length=200, blank=True)
    bill_postal = models.CharField(max_length=6, blank=True)
    bill_country = models.CharField(max_length=200, blank=True)
    # TODO: Django-countries: http://code.google.com/p/django-countries/

    # Shipping information:
    ship_as_bill = models.BooleanField(verbose_name="Ship to Billing?")  #If true ignore shipping
    ship_add_1 = models.CharField(max_length=200, blank=True)
    ship_add_2 = models.CharField(max_length=200, blank=True)
    ship_city = models.CharField(max_length=200, blank=True)
    ship_province = models.CharField(max_length=200, blank=True)
    ship_postal = models.CharField(max_length=6, blank=True)
    ship_country = models.CharField(max_length=200, blank=True)
    # TODO: Django-countries: http://code.google.com/p/django-countries/
        
    def __unicode__(self):
        return u'%s, %s' % (self.user, self.other_name) # Note 'u' prefix makes unicode string

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
    

class Subscription(models.Model):
    """
    Subscription defines the purchase of the product, which has
    an associated duration, for products with more than 1 term.
    For example, a 12 issue magazine subscription.
    """

    payee_key = models.ForeignKey('subs.Customer',
                                  verbose_name='Payee',
                                  related_name='subs_payee')

    promo_key = models.ForeignKey('products.Promo',
                                  verbose_name='Promo',
                                  related_name='subs_promo',
                                  blank=True, null=True)
    
    product_key = models.ForeignKey('products.Product',
                                    verbose_name='Product',
                                    related_name='subs_product')

    term_length = models.IntegerField() # eg. "2" (issues)

    TERM_UNITS = (
        ('Days',    'Days'),
        ('Weeks',   'Weeks'),
        ('Months',  'Months'),
        ('Years',   'Years'),
        ('Issues',  'Issues'),
    )

    term_units = models.CharField('Term units',
                                  max_length=6,
                                  choices=TERM_UNITS,
                                  default='Issues')

    STATUSES = (
        ('Inactive',    'Inactive'),
        ('Active',      'Active'),
        ('Closed',      'Closed'),
        ('Hold',        'Hold'),
    )

    status = models.CharField(max_length=8,
                              choices=STATUSES,
                              default='Active')

    gift_bool = models.BooleanField('Gift?', default=False)
    gift_name = models.CharField('Giftee name', max_length=100,blank=True)
    gift_msg = models.CharField('Git message', max_length=250,blank=True)
 
    def __unicode__(self):
        return u'%s - %s: %s %s' % (self.payee_key,
                                    self.product_key,
                                    self.term_length,
                                    self.term_units)


class Payment(models.Model):

    PAYMENT_METHODS = (
        ('Credit',  'Credit card'),
        ('Cheque',  'Cheque'),
        ('Cash',    'Cash'),
        ('Gift',    'Gift card'),
        ('Paypal',  'Paypal'),
        ('Interac', 'Interac'),
    )

    subscription = models.ForeignKey(Subscription)
    method = models.CharField('Payment method',
                              max_length=7,
                              choices=PAYMENT_METHODS)

    amount = models.DecimalField('Total',
                                 max_digits=9,
                                 decimal_places=2)   # Max 9,999,999.99

    def __unicode__(self):
        return u'%s - %s for $%.2f' % (self.subscription, self.method, self.amount)


