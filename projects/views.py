from audioop import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Project
from .forms import PasswordForm
from app import urls as urls_app
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404

# Create your views here.

def list(request):
    limit = 5
    page = request.GET.get("page", 1)
    keyword = request.GET.get("keyword")
    print(keyword)
    if keyword:
        project_list = Project.objects.filter(title__icontains=keyword)
    else:
        project_list = Project.objects.all()

    #paging
    project_paginator = Paginator(project_list.order_by("-date").values(), limit)
    try:
        project_paginator = project_paginator.page(page)
    except PageNotAnInteger:
        project_paginator = project_paginator.page(1)
    except EmptyPage:
        project_paginator = project_paginator.page(project_paginator.num_pages)

    context = {
        "Projects": project_paginator,
        "keyword": keyword if keyword else "",
    }
    return render(request, 'pages/allprojects.html', context)
# @login_required
# def project(request, id):
#     # Lấy dự án hoặc ném lỗi 404 nếu không tìm thấy
#     project = get_object_or_404(Project, id=id)

#     if request.method == 'POST':
#         form = PasswordForm(request.POST)
#         if form.is_valid():
#             password = form.cleaned_data['password']
#             # Kiểm tra mật khẩu
#             if password == project.project_password:
#                 # Nếu mật khẩu đúng, hiển thị trang dự án
#                 return render(request, 'pages/project.html', {'project': project})
#             else:
#                 # Nếu mật khẩu không đúng, hiển thị form nhập lại mật khẩu với thông báo lỗi
#                 error_message = "Mật khẩu không đúng. Vui lòng thử lại."
#                 return render(request, 'pages/inputpassword.html', {'form': form, 'error_message': error_message})
#     else:
#         form = PasswordForm()
#     return render(request, 'pages/inputpassword.html', {'form': form})
def project(request, slug):
    # Lấy dự án hoặc ném lỗi 404 nếu không tìm thấy
    project = get_object_or_404(Project, slug=slug)

    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data['password']
            # Kiểm tra mật khẩu
            if password == project.project_password:
                # Nếu mật khẩu đúng, hiển thị trang dự án
                return render(request, 'pages/project.html', {'project': project})
            else:
                # Nếu mật khẩu không đúng, hiển thị form nhập lại mật khẩu với thông báo lỗi
                error_message = "Mật khẩu không đúng. Vui lòng thử lại."
                return render(request, 'pages/inputpassword.html', {'form': form, 'error_message': error_message})
    else:
        form = PasswordForm()
    return render(request, 'pages/inputpassword.html', {'form': form})


