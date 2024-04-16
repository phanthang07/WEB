from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.list, name='projects'),
    path('<int:id>/', views.project, name='project'),

]
