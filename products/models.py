from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)
    issue_no = models.IntegerField(help_text='Current issue number')
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.issue_no)

class Promo(models.Model):

    name = models.CharField(max_length=200)
    dateCreated = models.DateField('Created', blank=True, null=True)
    # TODO: Limit discount to max 100
    discount = models.PositiveIntegerField(
            help_text="% discount (ex: '20')")
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.discount)

class SaleItem(models.Model):
    
    product = models.ForeignKey(Product)

    # max cost is $999,999,999.00
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    term = models.IntegerField(help_text='Number of issues')

    code = models.CharField(max_length=50)
    def __unicode__(self):
        return u'%s: %s - $%s' % (self.code, self.product, self,cost)
