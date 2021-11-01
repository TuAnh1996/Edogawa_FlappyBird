from django.db import models
from django.conf import settings



# như này đầu tiên mình tạo class xong mình phải makemigrations nó để liên kết với bản xong đó migrate để cập nhật nó 

# sau đó python manage.py makemigrations polls để báo với sql là ta vừa tạo 1 cái poll 
# sau đó ta sd python manage.py migrate để cập nhật

class Comment(models.Model):
    
#   <class 'polls.admin.CommentInline'>: (admin.E202) 'polls.Commenttt' has no ForeignKey to 'polls.Poll'.
    # comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')

    # ta khai báo field post là khóa ngoại liên kết với bảng Post, tham số on_delete Kteam cho nó thuộc loại CASCADE (có nghĩa là khi xóa bài viết thì xóa luôn bình luận), tham số related_name có nghĩa khi dev muốn tìm các bình luận từ một bài viết thì thông qua từ khóa ‘comments’ từ post
    # NameAcc = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # tương tự author là khóa ngoại liên kết bảng user của hệ thống Django để biết ai là người bình luận bài viết.
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
class Commenttt(models.Model):
    # commenttt = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)