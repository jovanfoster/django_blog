from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),    
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/create/', views.create_post, name='post-create'),
    path('post/<int:pk>/update/', views.update_post, name='post-update'),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),

]