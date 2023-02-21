from django.shortcuts import render,redirect
from .forms import BlogForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import NewsArticle, Blog
import requests
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def news_list(request):
    response = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=032a7b68408a4127a7fe5d90e71c983f')
    news_articles = response.json()['articles']
    context = {'news_articles': news_articles}
    return render(request, 'news_list.html', context)

def news_detail(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    context = {'article': article}
    return render(request, 'news_detail.html', context)

def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)
    context = {'blogs': blogs}
    return render(request, 'Blogs_list.html', context)



def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs_details.html', {'blog': blog})




def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            blog.author = request.user
            blog.save()
            return redirect('blog_list')
    else:
        form = BlogForm()
    context = {'form': form}
    return render(request, 'blog_form.html', context)




def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author == request.user:
        blog.delete()
    return redirect('blog_list')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user=form.save()
            user = authenticate(request, email=email, password=password)
            login(request, user)
            messages.success(request, f'Account created for {email}!')
            return redirect('user_login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

from .forms import LoginForm


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news_list')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

