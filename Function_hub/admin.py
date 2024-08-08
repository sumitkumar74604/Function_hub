from django.contrib import admin
from .models import UserRegistration, ContactMessage

@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'mobile_no')
    search_fields = ('first_name', 'last_name', 'email', 'mobile_no')
    ordering = ('-email',)  # Orders by email in descending order

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('contact_message_id', 'Contact_name', 'Contact_email', 'Contact_subject', 'contact_sent_at')
    search_fields = ('Contact_name', 'Contact_email', 'Contact_subject')
    list_filter = ('contact_sent_at',)  # Adds a filter by the date when the contact message was sent
    ordering = ('-contact_sent_at',)  # Orders messages by the latest first
    readonly_fields = ('contact_message_id', 'contact_sent_at')  # Makes these fields read-only
