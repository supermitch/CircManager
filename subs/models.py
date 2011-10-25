from django.db import models

# Create your models here.
class Customer(models.Model):
    f_name = models.CharField('First Name', max_length=200)
    l_name = models.CharField('Last Name', max_length=200)
    o_name = models.CharField('Other Names', max_length=200)
    b_day = models.DateField('Birthday')
    phone = models.IntegerField()
    email = models.EmailField()
    bill_add_1 = models.CharField(max_length=200)
    bill_add_2 = models.CharField(max_length=200)
    bill_city = models.CharField(max_length=200)
    bill_country = models.CharField(max_length=200)
    bill_postal = models.CharField(max_length=6)
    bill_province = models.CharField(max_length=200)
    ship_add_1 = models.CharField(max_length=200)
    ship_add_2 = models.CharField(max_length=200)
    ship_city = models.CharField(max_length=200)
    ship_country = models.CharField(max_length=200)
    ship_postal = models.CharField(max_length=6)
    ship_province = models.CharField(max_length=200)
        
    def __unicode__(self):
        return self.f_name 