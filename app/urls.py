from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),    
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/<int:pk>/update/', views.update_post, name='post-update'),

]