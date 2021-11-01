from django.urls import path  # cái path này dùng để định nghĩ các url
from . import views
from django.urls import path, include
from django.conf.urls import handler404,url
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path là  đường dẫn trắng chính là xử lý cho urls http://localhost:8000/polls
    path('', views.home),
    path('contact/', views.contact, name='contact'),
    path('ContactComment/', views.ContactComment, name='ContactComment'),

    path('home/', views.home, name='home'),
    path('polls/', views.polls, name='polls'),
    path('Blogpost/', include('Blogpost.urls')),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="pages/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page='/polls'), name='logout'),
]

handler404 = 'polls.views.error'
