from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.conf import settings
from .models import UserRegistration, UserLogin, ContactMessage
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login as auth_login
from django.core.mail import send_mail
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

curl = settings.CURRENT_URL 

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html', {'curl': curl})

def checkout(request):
    return render(request, 'checkout.html', {'curl': curl})

def details(request):
    return render(request, 'details.html', {'curl': curl})

def shop(request):
    return render(request, 'shop.html', {'curl': curl})


@csrf_protect
def contact(request):
    print("Contact view called")
    msg = ""
    
    if request.method == 'POST':
        print("POST request received")
        Contact_name = request.POST.get('Contact_name')
        Contact_email = request.POST.get('Contact_email')
        Contact_subject = request.POST.get('Contact_subject')
        Contact_message = request.POST.get('Contact_message')
        
        # Basic validation
        if not Contact_name or not Contact_email or not Contact_subject or not Contact_message:
            msg = "All fields are required."
            return render(request, 'contact.html', {'curl': settings.CURRENT_URL, 'msg': msg})

        # Validate email
        try:
            validate_email(Contact_email)
        except ValidationError:
            msg = "Invalid email address."
            return render(request, 'contact.html', {'curl': settings.CURRENT_URL, 'msg': msg})

        try:
            # Save contact message to the database
            ContactMessage.objects.create(
                Contact_name=Contact_name,
                Contact_email=Contact_email,
                Contact_subject=Contact_subject,
                Contact_message=Contact_message
            )
                                
            # Send email
            send_mail(
                subject=f"Contact Form Submission: {Contact_subject}",
                message=f"Name: {Contact_name}\nEmail: {Contact_email}\n\nMessage:\n{Contact_message}",
                from_email=Contact_email,  # Use the sender's email from the form
                recipient_list=[settings.CONTACT_EMAIL],  # Always send to this receiver's email
            )
            
            # Print success message to the terminal
            print(f"Message sent successfully! Name:{Contact_name} Email:{Contact_email} Subject:{Contact_subject} Message:{Contact_message}")

            msg = "Your message has been sent successfully!"
            return render(request, 'contact.html', {'curl': settings.CURRENT_URL, 'msg': msg})
        
        except Exception as e:
            msg = f"Failed to send message: {str(e)}"
            print(f"Exception occurred: {str(e)}")
            return render(request, 'contact.html', {'curl': settings.CURRENT_URL, 'msg': msg})
    
    return render(request, 'contact.html', {'curl': settings.CURRENT_URL, 'msg': msg})
@csrf_protect
def login(request):
    msg = ""
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            
            if user is not None:
                auth_login(request, user)
                msg = "Login successful!"
                return render(request, 'login.html', {'curl': curl, 'msg': msg})  
            else:
                msg = "Invalid email or password."
                return render(request, 'login.html', {'curl': curl, 'msg': msg})
        
        except Exception as e:
            msg = f"An error occurred: {str(e)}"
            return render(request, 'login.html', {'curl': curl, 'msg': msg})

    return render(request, 'login.html', {'curl': curl, 'msg': msg})

@csrf_protect
def Register(request):
    msg = ""
    if request.method == 'POST':
        # Retrieve form data from POST request
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        mobile_no = request.POST.get('mobile_no')
        address1 = request.POST.get('address1')
        address2 = request.POST.get('address2', '')  # Default to empty string if not provided
        country = request.POST.get('country')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        
        # Create and save a new UserRegistration instance
        user_registration = UserRegistration(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            mobile_no=mobile_no,
            address1=address1,
            address2=address2,
            country=country,
            city=city,
            state=state,
            zip_code=zip_code
        )
        try:
            print(user_registration)
            user_registration.save()
            msg = "Registration successful!"
            return render(request, 'Register.html', {'curl': curl, 'msg': msg})  # Use the URL name for the registration page
        except Exception as e:
            msg = f"Registration failed: {str(e)}"
            return render(request, 'Register.html', {'curl': curl, 'msg': msg})
    
    return render(request, 'Register.html', {'curl': curl})