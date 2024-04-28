from django.urls import include, path
from . import views

# urlpatterns = [
#     path('', views.list, name='projects'),
#     path('<int:id>/', views.project, name='project'),

# ]


urlpatterns = [
    path('', views.list, name='projects'),
    path('<slug:slug>/', views.project, name='project'), # Sử dụng slug thay vì id
]
