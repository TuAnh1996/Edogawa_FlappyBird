
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import handler404
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),#ta sẽ liên cái web với nhau hiểu đơn giản cta liên cái project mysite với cái web sever bằng cái url 
    #nếu path('polls' thì hiểu đơn giản urls của app polls sẽ do áp pollsquar lý muốn vào nó thì phải qua polls còn nếu dể '' ntn thfi nó chạy thằng tới hàm index trg views 
    path('Blogpost/', include('Blogpost.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)