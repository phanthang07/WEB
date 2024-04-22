from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Comment
from posts.forms import CommentForm
from django.http import HttpResponseRedirect

# Create your views here.
def list(request):
    limit = 5
    page = request.GET.get("page", 1)
    keyword = request.GET.get("keyword")

    if keyword:
        posts_list = Post.objects.filter(title__icontains = keyword)
    else:
        posts_list = Post.objects.all()
    posts_list = posts_list.order_by("-date").values()

    #paging
    posts_paginator = Paginator(posts_list, limit)
    try:
        posts_paginator = posts_paginator.get_page(page)
    except PageNotAnInteger:
        posts_paginator = posts_paginator.get_page(1)
    except EmptyPage:
         posts_paginator = posts_paginator.get_page(posts_paginator.num_pages)

    context = {
        "Posts": posts_paginator,
        "keyword": keyword if keyword else "",
    }
    return render(request, 'pages/allposts.html', context)

# def post(request, id):
#     project = Post.objects.get(id=id)
#     return render(request, 'pages/post.html', {'post':post})

# def post(request, id):
#     post = get_object_or_404(Post, id=id)
#     form = CommentForm()
#     if request.method =='POST':
#         form = CommentForm(request.POST, author=request.user,post=post)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(request.path)
#     return render(request, 'pages/post.html', {'post':post,'form':form})
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .forms import CommentForm  # Đảm bảo import đúng form CommentForm
from .models import Post

def post(request, id):
    post = get_object_or_404(Post, id=id)
    form = CommentForm()
    comments = post.comments.all()  # Lấy tất cả các bình luận của bài viết
    if request.method == 'POST':
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            # Sau khi lưu bình luận, bạn cần làm mới form để chuẩn bị cho bình luận mới
            form = CommentForm()
            # Đảm bảo bạn lấy danh sách bình luận mới sau khi thêm
            comments = post.comments.all()
    return render(request, 'pages/post.html', {'post': post, 'form': form, 'comments': comments})

