from django.urls import path

from app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    # path('customer/', views.customer, name='customer'),
    path('service/', views.service, name='service'),
    path('contact/', views.contact, name='contact'),
    path('thank/', views.thank, name='thank'),
]
