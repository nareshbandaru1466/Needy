from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    """Home page view that will serve your React app"""
    return render(request, 'index.html')  # We'll create this template later
