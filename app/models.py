from django.db import models 
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)
    name = models.CharField(null=True, blank=True, max_length=200)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(default='user.png')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'user'
        ordering = ['name'] 


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table = 'category'
        verbose_name_plural = 'categories'


class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    body = models.TextField()
    photo = models.ImageField(null=True, blank=True, help_text='Select a picture for your post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title + "\n" + self.body[0:50]

    class Meta:
        db_table = 'post'
        ordering = ['-updated_at', '-created_at']


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return  self.body[0:5]

    class Meta:
        db_table = 'comment'
