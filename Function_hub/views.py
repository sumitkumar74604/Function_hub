from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from django.conf import settings

curl = settings.CURRENT_URL 

def index(request):
    return render(request, 'index.html')

def cart(request):
    return render(request, 'cart.html', {curl: 'curl'})

def checkout(request):
    return render(request, 'checkout.html', {curl: 'curl'})

def contact(request):
    return render(request, 'contact.html', {curl: 'curl'})

def details(request):
    return render(request, 'details.html', {curl: 'curl'})


def shop(request):
    return render(request, 'shop.html', {curl: 'curl'})