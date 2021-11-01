from .forms import RegistrationForm
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse

from .forms import CommentCreateForm, CommentttCreateForm
from .models import Comment, Commenttt


# def polls(request):
#    return render(request, 'pages/polls.html')

# def contact(request):
#    return render(request,"pages/contact.html")


def home(request):
   return render(request, "pages/home.html")


def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})


def polls(request):

    form = CommentttCreateForm()
    if request.method == "POST":
        form = CommentttCreateForm(request.POST, author=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    context = {
        'Commenttt_list': Commenttt.objects.all(),
        'form': CommentttCreateForm(),
    }
    return render(request, 'pages/polls.html', context)


def contact(request):

    form = CommentCreateForm()
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    context = {
        'Comment_list': Comment.objects.all(),
        'form': CommentCreateForm(),
    }
    return render(request, "pages/contact.html", context)


def ContactComment(request):
    form = CommentCreateForm()
    # nó sẽ gọi cái from rồi nếu method post( action="{% url 'ContactComment' %}" method="POST") thì nó chạy vào save r return  
    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "pages/ContactComment.html")
