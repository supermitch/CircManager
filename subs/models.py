from django.db import models
from django.forms import ModelForm

# Create your models here.
class Customer(models.Model):

    GREETING_CHOICES = (
        ('Mr',      'Mr.'),
        ('Mrs',     'Mrs.'),
        ('Ms',      'Ms.'),
        ('Dr',      'Dr.'),
        ('Prof',    'Prof.'),
    )

    # Customer personal details
    greeting = models.CharField('Greeting', max_length=10, choices=GREETING_CHOICES, blank=True)
    first_name = models.CharField('First Name', max_length=50)
    last_name = models.CharField('Last Name', max_length=50)
    other_name = models.CharField('Other Names', max_length=100,blank=True)
    company = models.CharField('Company', max_length=100, blank=True)
    birthday = models.DateField('Birthday', blank=True, null=True)
    
    #Todo: we want only 0-9, '-', ' ', '.', 'x', 'ext', and '()' for phone. Use a validator!
    #from django.core.validators import RegexValidator 
    #import re 
    #phone_regex = re.compile(r'[^A-Za-z0-9 _.-()]+$') # This is what needs work...
    #phone = models.CharField(max_length = 20, unique =False, blank=True, validators=[RegexValidator(regex=phone_regex)] ) 

    phone = models.CharField('Phone number', max_length=50, blank=True)
    email = models.EmailField(blank=True)

    # Billing information
    bill_add_1 = models.CharField(max_length=200, blank=True)
    bill_add_2 = models.CharField(max_length=200, blank=True)
    bill_city = models.CharField(max_length=200, blank=True)
    bill_province = models.CharField(max_length=200, blank=True)
    bill_postal = models.CharField(max_length=6, blank=True)
    bill_country = models.CharField(max_length=200, blank=True)
    # todo: Django-countries: http://code.google.com/p/django-countries/

    # Shipping information:
    ship_as_bill = models.BooleanField(verbose_name="Ship to Billing?")  #If true ignore shipping
    ship_add_1 = models.CharField(max_length=200, blank=True)
    ship_add_2 = models.CharField(max_length=200, blank=True)
    ship_city = models.CharField(max_length=200, blank=True)
    ship_province = models.CharField(max_length=200, blank=True)
    ship_postal = models.CharField(max_length=6, blank=True)
    ship_country = models.CharField(max_length=200, blank=True)
        # todo: Django-countries: http://code.google.com/p/django-countries/
        
    def __unicode__(self):
        return u'%s, %s' % (self.last_name, self.first_name) # Note 'u' prefix makes unicode string

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
    

class Subscription(models.Model):

    TERM_UNIT_CHOICES = (
        ('Days',    'Days'),
        ('Weeks',   'Weeks'),
        ('Months',  'Months'),
        ('Years',   'Years'),
    )
    payee_key = models.ForeignKey(Customer, verbose_name="Payee", related_name='subs_payee')
    # reader_key can be same (or not) as payee_key:
    reader_key = models.ForeignKey(Customer, verbose_name="Reader", related_name='subs_reader')

    # Need to define Promos and Products Models, but I think these should reside in a Products App
    #promo_key = models.ForeignKey('products.Promo', verbose_name="Promo", related_name='subs_promo')
    #product_key = models.ForeignKey('products.Product', verbose_name="Product", related_name='subs_product')
    term_length = models.IntegerField()                         # eg. "2" (months)
    term_units = models.CharField("Term units", max_length=6, choices=TERM_UNIT_CHOICES)  # eg. "months"

    def __unicode__(self):
        return u'%s - %s %s' % (self.payee_key, self.term_length, self.term_units)

class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('Credit',  'Credit card'),
        ('Cheque',  'Cheque'),
        ('Cash',    'Cash'),
        ('Gift',    'Gift card'),
        ('Paypal',  'Paypal'),
        ('Interac', 'Interac'),
    )

    subscription = models.ForeignKey(Subscription)
    method = models.CharField('Payment method', max_length=7, choices=PAYMENT_METHOD_CHOICES)
    amount = models.DecimalField('Total', max_digits=9, decimal_places=2)   # Max value is 9,999,999.99

    def __unicode__(self):
        return u'%s - %s for $%.2f' % (self.subscription, self.method, self.amount)


