from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=200)
    dateCreated = models.DateField('Created', blank=True, null=True)
    term = models.IntegerField(help_text="Enter number of issues")

    # max cost is $999,999,999.00
    cost = models.DecimalField(max_digits=8, decimal_places=2)
    code = models.CharField("Product code", max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s - %s' % (self.code, self.name, self.term)

class Promo(models.Model):

    name = models.CharField(max_length=200)
    dateCreated = models.DateField('Created', blank=True, null=True)
    # TODO: Limit discount to max 100
    discount = models.PositiveIntegerField(
            help_text="% discount (ex: '20')")
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s' % (self.name, self.discount)

