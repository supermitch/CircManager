from subs.models import Customer, Subscription, Payment
from django.contrib import admin
from django.contrib.auth.models import User

class CustomerAdmin(admin.ModelAdmin):

    def user_first_name(self, instance):
        return instance.user.first_name

    def user_last_name(self, instance):
        return instance.user.last_name

    def user_email(self, instance):
        return instance.user.email

    # defines what appears on Customers admin page (list of entries)
    list_display = ('user', 'user_first_name', 'user_last_name') 

    # get user fields to display in Customer admin form, below.
    # (list_display) values won't work
    readonly_fields = ('user_first_name', 'user_last_name', 'user_email')

    fieldsets = (
        ('Personal information', {
            'fields': (('greeting',
                        'user_first_name',
                        'other_name',
                        'user_last_name'),
                        'company',
                        'user_email',
                        'phone',
                        'birthday')
        }),
        
        ('Billing information', {
            # 'classes': ('collapse',),
            'fields': ('bill_add_1',
                       'bill_add_2',
                       'bill_city',
                       'bill_province',
                       'bill_postal',
                       'bill_country')
        }),

        (None, {
            'fields': ['ship_as_bill']
        }),

        ('Shipping information', {
            'classes': ('collapse',),   # CSS: 'collapse' hides it.
            'fields': ('ship_add_1',
                       'ship_add_2',
                       'ship_city',
                       'ship_province',
                       'ship_postal',
                       'ship_country')
        }),
    )
    
    # Other stuff from the tutorial:
    #inlines = [ChoiceInline]
    #list_filter = ['pub_date']
    #search_fields = ['question']
    #date_hierarchy = 'pub_date'

class SubscriptionAdmin(admin.ModelAdmin):
    pass

class PaymentAdmin(admin.ModelAdmin):
    pass

# TODO: Check to see if there's a better way
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Subscription, SubscriptionAdmin) 
admin.site.register(Payment, PaymentAdmin)
