from django.shortcuts import render, redirect
from .models import User, Post, Category, Comment
from .forms import PostForm, RegisterForm, UpdateUserForm, UpdateCommentForm
from django.contrib.auth import login
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import HttpResponse

# Create your views here.
def sign_up(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    context = {'form':form}
    return render(request, 'registration/sign_up.html', context)

def update_user(request):
    user = request.user
    form = UpdateUserForm(instance = user)
    if request.method == 'POST':
        form = UpdateUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home', 1)
    context = {'form':form}
    return render(request, 'app/update-user.html', context)


def profile(request,pk):
    user = User.objects.get(id =pk)
    posts = user.post_set.all()
    comments = user.comment_set.all()
    context = {'user':user, 'posts':posts, 'comments':comments}
    return render(request, 'app/profile.html', context)


def home(request, page):
    if request.GET.get('q'):
        q = request.GET.get('q')
    else:
        q = ''
    
    categories = Category.objects.all()
    posts = Post.objects.filter(
        Q(title__icontains=q) |
        Q(body__icontains=q) |
        Q(category__name__icontains=q) |
        Q(author__name__icontains=q)    
    )
    comments = Comment.objects.filter(
        Q(user__name__icontains = q) |
        Q(body__icontains = q) |
        Q(post__category__name__icontains = q)   
    )
    
    paginator = Paginator(posts, per_page=3)
    page_object = paginator.get_page(page)
    
    context = {
        'posts':posts, 
        'categories':categories,
        'comments':comments,  
        'page_object':page_object,
        'q':q
 
    }
    return render(request, 'app/home.html', context)

@login_required(login_url='login')
def create_post(request):
    if request.user.is_superuser:
        form = PostForm()
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.title = post.title.capitalize()
                post.save()
                return redirect('home', 1)
        context = {'form':form}
        return render(request, 'app/create-post.html', context)
    else:
        return HttpResponse('You are not allowed to make a post ')

@login_required(login_url='login')
def get_post(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == 'POST':
        Comment.objects.create (
            user = request.user,
            body = request.POST.get('comment'),
            post = post
        )
        return redirect('get_post', pk=post.pk)
    comments = post.comment_set.all()
    context = {'post':post, 'comments':comments}
    return render(request,'app/get-post.html', context)

@login_required
def add_category(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            category = request.POST['category']
            Category.objects.create(name=category)
            return redirect('home', 1)
        
        return render(request, 'app/add_category.html')

@login_required(login_url='login')
def update_post(request, pk):
    post = Post.objects.get(id=pk)  
    form = PostForm(instance=post)
    if post.author == request.user:
        if request.method == 'POST':
            form = PostForm(request.POST,request.FILES, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.title = post.title.capitalize()
                post.save()
                return redirect('get_post', pk=post.id)
    context = {'form':form}
    return render(request, 'app/update-post.html', context)

@login_required(login_url='login')
def update_comment(request, pk):
    comment = Comment.objects.get(id=pk)
    form = UpdateCommentForm(instance=comment)
    if request.method == 'POST':
        form = UpdateCommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('get_post', pk=comment.post.pk)
    return render(request, 'app/update_comment.html', {'form':form})


def delete_post(request, pk):
    page = request.GET.get('page')
    post = Post.objects.get(id=pk) 
    if post.author == request.user:
        if request.method == 'POST':
            post.delete()
            return redirect('home', 1)
    return render(request, 'app/delete.html', {'obj':post.title})


def delete_comment(request, pk):
    comment = Comment.objects.get(id=pk) 
    if comment.user == request.user:
        if request.method == 'POST':
            comment.delete()
            return redirect('get_post', pk=comment.post.id)
    return render(request, 'app/delete.html', {'obj':comment})







