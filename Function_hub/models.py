from django.db import models

class UserRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=150)  # Note: Storing passwords in plain text is not secure
    mobile_no = models.CharField(max_length=15)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"First Name: {self.first_name}, "
            f"Last Name: {self.last_name}, "
            f"Email: {self.email}, "
            f"Password: {self.password}, "  # Note: Storing passwords in plain text is not secure
            f"Mobile No: {self.mobile_no}, "
            f"Address1: {self.address1}, "
            f"Address2: {self.address2 or 'N/A'}, "
            f"Country: {self.country}, "
            f"City: {self.city}, "
            f"State: {self.state}, "
            f"ZIP Code: {self.zip_code}, "
            f"Created At: {self.created_at}, "
            f"Updated At: {self.updated_at}"
        )

    class Meta:
        verbose_name = 'User Registration'
        verbose_name_plural = 'User Registrations'

    
class UserLogin(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)  # ForeignKey to UserRegistration
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=150)  # Note: Storing passwords in plain text is not secure
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"User ID: {self.user.id}, "
            f"Email: {self.email}, "
            f"Password: {self.password}, "  # Note: Storing passwords in plain text is not secure
            f"Created At: {self.created_at}, "
            f"Updated At: {self.updated_at}"
        )

    class Meta:
        verbose_name = 'User Login'
        verbose_name_plural = 'User Logins'

class ContactMessage(models.Model):
    contact_message_id = models.AutoField(primary_key=True)
    Contact_name = models.CharField(max_length=100)
    Contact_email = models.EmailField(max_length=100)
    Contact_subject = models.CharField(max_length=200)
    Contact_message = models.TextField()
    contact_sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"Contact_ID: {self.contact_message_id}, "
            f"Contact_name: {self.Contact_name}, "
            f"Contact_email: {self.Contact_email}, "
            f"Contact_subject: {self.Contact_subject}, "
            f"Contact_message: {self.Contact_message[:1000]}..."  # Displaying first 1000 characters for brevity
        )

class Meta:
    indexes = [
        models.Index(fields=['contact_sent_at']),
    ]
    ordering = ['-contact_sent_at']  # Default ordering by date, most recent first

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name='states', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.country.name})"
    
class BillingAddress(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly adding an ID field
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Making email unique
    mobile = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.address_line_1}, {self.city}'

    class Meta:
        verbose_name = 'Billing Address'
        verbose_name_plural = 'Billing Addresses'

class ShippingAddress(models.Model):
    id = models.AutoField(primary_key=True)  # Explicitly adding an ID field
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)  # Unique constraint is not applied here; you can add it if needed
    mobile = models.CharField(max_length=20)
    address_line_1 = models.CharField(max_length=255)
    address_line_2 = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.address_line_1}, {self.city}'

    class Meta:
        verbose_name = 'Shipping Address'
        verbose_name_plural = 'Shipping Addresses'
