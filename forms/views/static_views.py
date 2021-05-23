from django.shortcuts import render
from django.contrib.auth.decorators import login_required



def index(request):
    """basic home page"""
    return render(request, "base.html")

def thank_you(request):
    """after registration page"""
    return render(request, "forms/thank_you.html")

@login_required
def user_home(request):
    """ user home_page after login"""
    return render(request, "forms/user_home.html")






