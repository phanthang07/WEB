# from django.urls import include, path
# from . import views

# urlpatterns = [
#     path('', views.list, name='posts'),
#     path('<int:id>/', views.post, name='post'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list, name='posts'),
    path('<slug:slug>/', views.post, name='post'),
]
