from django.db import models

class UserRegistration(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=150)
    mobile_no = models.CharField(max_length=15)
    address1 = models.CharField(max_length=300)
    address2 = models.CharField(max_length=300, blank=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    
    def __str__(self):
        return (
            f"ID: {self.id}, "
            f"First Name: {self.first_name}, "
            f"Last Name: {self.last_name}, "
            f"Email: {self.email}, "
            f"Password: {self.password}, "  # Corrected spelling
            f"Mobile No: {self.mobile_no}, "
            f"Address1: {self.address1}, "
            f"Address2: {self.address2 or 'N/A'}, "
            f"Country: {self.country}, "
            f"City: {self.city}, "
            f"State: {self.state}, "
            f"ZIP Code: {self.zip_code}"
        )



class UserLogin(models.Model):
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=150) 

    def __str__(self):
        return (
            f"Email: {self.email}, "
            f"Password: {self.password}, "
        )


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