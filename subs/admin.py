from subs.models import Customer, Subscription
from django.contrib import admin

class CustomerAdmin(admin.ModelAdmin):

    # fieldset docs: https://docs.djangoproject.com/en/dev/ref/contrib/admin/#django.contrib.admin.ModelAdmin.fieldsets

    list_display = ('last_name', 'first_name')  # defines what appears on Customers admin page (list of entries)

    fieldsets = (   # Defines presentation of data in groups during Customer record editing
        ('Personal information', {
            'fields': (('first_name', 'last_name', 'other_name'), 'email', 'phone', 'birthday')
        }),
        
        ('Billing information', {
            # 'classes': ('collapse',),
            'fields': ('bill_add_1', 'bill_add_2', 'bill_city', 'bill_province', 'bill_postal', 'bill_country')
        }),
        (None, {
            'fields': ['ship_as_bill']
        }),
        ('Shipping information', {
            'classes': ('collapse',),   # Class defines CSS applied to this fieldset. 'collapse' hides it.
            'fields': ('ship_add_1', 'ship_add_2', 'ship_city', 'ship_province', 'ship_postal', 'ship_country')
        }),
    )
    
    # Other stuff from the tutorial:
    #inlines = [ChoiceInline]
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Subscription) # Todo: Check to see if there's a better way

