from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from .models import CreateUserForm
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        # Thực hiện gửi email
        send_mail(
            'Thông tin liên hệ từ khách hàng',  # Chủ đề của email
            f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',  # Nội dung của email
            'monster09422001@gmail.com',  # Địa chỉ email bạn muốn nhận email từ form
            ['phanvanthangphan07@gmail.com'],  # Danh sách các địa chỉ email nhận
            fail_silently=False,
        )
        # Chuyển hướng người dùng sau khi gửi thành công
        return redirect('thank')
    return render(request, "pages/index.html")

def customer(request):
    return render(request, "pages/customer.html")

def service(request):
    return render(request, "pages/service.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email', '')
        message = request.POST.get('message', '')
        # Thực hiện gửi email
        send_mail(
            'Thông tin liên hệ từ khách hàng',  # Chủ đề của email
            f'Name: {name}\nPhone: {phone}\nEmail: {email}\nMessage: {message}',  # Nội dung của email
            'monster09422001@gmail.com',  # Địa chỉ email bạn muốn nhận email từ form
            ['phanvanthangphan07@gmail.com'],  # Danh sách các địa chỉ email nhận
            fail_silently=False,
        )
        # Chuyển hướng người dùng sau khi gửi thành công
        return redirect('thank')
    return render(request, 'pages/contact.html')

def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Đăng ký thành công!')
            return redirect('signin')
        else:
            # Lưu ý: errors là một từ điển chứa tất cả các thông báo lỗi cho mỗi trường
            # Bạn có thể lặp qua nó và truy xuất các thông báo lỗi cho từng trường cụ thể.
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field.capitalize()}: {error}')
            return redirect('signup')
    context = {'form': form}
    return render(request, "pages/signup.html", context)

def signin(request):
    if request.user.is_authenticated:
        # User is already authenticated, redirect to home
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Logged In Successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    context = {}
    return render(request, "pages/signin.html", context)

def thank(request):
    return render(request, 'pages/thankyouforcontact.html')

def signout(request):
        logout(request)
        messages.success(request, "Logged Out Successfully!!")
        return redirect('home')

def err404(request):
    return render(request, 'pages/error.html')