from django.shortcuts import render
from .models import Customers
# Create your views here.
def showCustomers(requste ):
    customers = Customers.objects.all() 
    return render(requste , 'client/ClientHomePage.html' ,{'customers':customers})

def loginPage(requste):
    return render(requste , 'client/login.html')

def createAccount (requste):
    return render(requste , 'client/signup.html')