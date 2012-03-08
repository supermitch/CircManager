from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    dateCreated = models.DateField('Created', blank=True, null=True)
    term = models.IntegerField(help_text="Enter number of issues")
    cost = models.IntegerField()
    code = models.CharField("Product code", max_length=200)
    description = models.TextField()

    def __unicode__(self):
        return u'%s - %s - %s' % (self.code, self.name, self.term)

