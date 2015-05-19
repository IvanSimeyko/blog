from django.contrib import admin
from contacts.models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_email', 'contact_date']
    search_fields = ['contact_email', 'contact_email']
    list_filter = ['contact_date']


admin.site.register(Contact, ContactAdmin)