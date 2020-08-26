from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),    
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
]