from django.shortcuts import render
from customer.models import Customer

# Create your views here.
def list(request):
    # customers = Customer.objects.all()
    # return render(request, 'pages/customer.html', {'customers': customers})
    Data = {'Customers': Customer.objects.all()}
    return render(request, 'pages/customer.html', Data)
