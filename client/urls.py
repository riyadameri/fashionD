from django.urls import path, include
from . import views

urlpatterns = [
    path('HomePage', views.showCustomers),
    path('login', views.loginPage),
    path('signup', views.createAccount),
]
