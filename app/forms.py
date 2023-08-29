from .models import Post, Comment, User, Category 
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        exclude = ['author', 'comments']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'name', 'password1', 'password2']

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'name','bio', 'avatar']

class UpdateCommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
