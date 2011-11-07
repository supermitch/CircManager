from django.db import models

# Create your models here.
class Customer(models.Model):

    # Customer personal details
    f_name = models.CharField('First Name', max_length=50)
    l_name = models.CharField('Last Name', max_length=50)
    o_name = models.CharField('Other Names', max_length=100)
    b_day = models.DateField('Birthday')
    phone = models.IntegerField()
    email = models.EmailField()

    # Billing information
    bill_add_1 = models.CharField(max_length=200)
    bill_add_2 = models.CharField(max_length=200)
    bill_city = models.CharField(max_length=200)
    bill_country = models.CharField(max_length=200)
    bill_postal = models.CharField(max_length=6)
    bill_province = models.CharField(max_length=200)
    
    # Shipping information:
    ship_as_bill = models.BooleanField('Ship to Billing?')  #If true ignore shipping
    ship_add_1 = models.CharField(max_length=200)
    ship_add_2 = models.CharField(max_length=200)
    ship_city = models.CharField(max_length=200)
    ship_country = models.CharField(max_length=200)
    ship_postal = models.CharField(max_length=6)
    ship_province = models.CharField(max_length=200)
        
    def __unicode__(self):
        return self.f_name

class Substription(models.Model):

    TERM_UNIT_CHOICES = (
        ('Day',   'Day'),
        ('Week',   'Week'),
        ('Month',   'Month'),
        ('Year',    'Year'),
    )
    payee_key = models.ForeignKey(Customer, verbose_name="Payee", related_name='subs_payee')
    # reader_key can be same (or not) as payee_key:
    reader_key = models.ForeignKey(Customer, verbose_name="Reader", related_name='subs_reader')

    # Need to define Promos and Products Models, but I think these should reside in a Products App
    #promo_key = models.ForeignKey('Promo', verbose_name="Promo", related_name='subs_promo')
    #product_key = models.ForeignKey('Product', verbose_name="Promo", related_name='subs_product')
    term_units = models.CharField("Term units", max_length=1, choices=TERM_UNIT_CHOICES)  # eg. "months"
    term_length = models.IntegerField()                         # eg. "2" (months)

    def __unicode__(self):
        return u'%s: %s %s' % (self.payee_id, self.term_length, self.term_units)
