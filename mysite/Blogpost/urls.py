from django.views.generic import ListView
from . import views
from django.urls import path
from .models import Post

urlpatterns = [
    path('', ListView.as_view(
      queryset = Post.objects.all().order_by('-date'),
      template_name = 'Blogpost/blog.html',
      context_object_name = 'Posts',
      paginate_by = 10)
      , name='Blogpost'),
  # path('<int:id>/', views.PostDetailView.as_view(),name='post'),
  path('<int:pk>/', views.post,name='post'),
 
]