from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from customer.models import Customer
from django.db.models import Q

def list(request):
    limit = 10  # Số khách hàng mỗi trang
    page = request.GET.get("page", 1)
    keyword = request.GET.get("keyword")

    # Tìm kiếm theo tên hoặc mã khách hàng
    if keyword:
        customer_list = Customer.objects.filter(
            Q(name__icontains=keyword) | Q(customercode__icontains=keyword)
        )
    else:
        customer_list = Customer.objects.all()

    # Phân trang
    paginator = Paginator(customer_list.order_by("id"), limit)
    try:
        customers_page = paginator.page(page)
    except PageNotAnInteger:
        customers_page = paginator.page(1)
    except EmptyPage:
        customers_page = paginator.page(paginator.num_pages)

    context = {
        "Customers": customers_page,      # Page object
        "keyword": keyword or "",         # Từ khóa tìm kiếm
    }

    return render(request, "pages/customer.html", context)
