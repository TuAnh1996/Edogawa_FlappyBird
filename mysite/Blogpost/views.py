from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from django.views.generic import ListView, DetailView
# Create your views here.
from .forms import CommentForm

from django.http import HttpResponseRedirect

class PostListView(ListView):
    queryset = Post.objects.all().order_by('-date')
    template_name = 'Blogpost/blog.html'
    context_object_name = 'Posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'Blogpost/post.html'
def post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "Blogpost/post.html", {"post": post, "form": form})