from django import forms
from django import forms
import re
from django.contrib.auth.models import User
from .models import Comment, Commenttt


class RegistrationForm(forms.Form):

    username = forms.CharField(label='username',  max_length=30)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='password', widget=forms.PasswordInput())
    password2 = forms.CharField(
        label='Re-password', widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2 and password1:
                return password2
        raise forms.ValidationError("Invalid password")

    def clean_username(self):
        username = self.cleaned_data['username']
        if re.search(r'^\w+&', username):
            raise forms.ValidationError("Invalid username")
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Account already exists")

    def save(self):
        User.objects.create_user(
            username=self.cleaned_data['username'], email=self.cleaned_data['email'], password=self.cleaned_data['password1'])


class CommentCreateForm(forms.ModelForm):

   
    class Meta:
        model = Comment
        fields = ('body',)
        # (tên tác giả và bài viết được comment không thể nhập tay được) nên khai báo fields chỉ có body để form chỉ tạo input body. tức ta chỉ hiện đc nd của nó thôi 


class CommentttCreateForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Kteam override phương thức khởi tạo, mục đích là lấy giá trị author và post để lưu vào bảng comment. Sau khi lấy xong thì ta gọi tiếp phương thức khởi tạo của class cha.
        self.author = kwargs.pop('author', None)
        # self.post = kwargs.pop('post', None)
        super().__init__(*args, **kwargs)
    def save(self, commit=True):
        # Kteam override phương thức save có sẵn của ModelForm, việc override này mục đích gán giá trị author và post. Đầu tiên là gọi phương thức save của class cha (ta cho tham số commit = False để chưa lưu xuống database). Sau đó lấy instance comment ra và gán giá trị author và post rồi mới gọi phương thức save() của model.
        # tham số commit = False để chưa lưu xuống database
        comment = super().save(commit=False)
        comment.author = self.author
        # comment.post = self.post
        comment.save()

    class Meta:
        model = Commenttt
        fields = ('body',)
        # (tên tác giả và bài viết được comment không thể nhập tay được) nên khai báo fields chỉ có body để form chỉ tạo input body. tức ta chỉ hiện đc nd của nó thôi 
