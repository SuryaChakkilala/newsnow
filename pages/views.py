from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterUserForm, UserUpdateForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    context = {}
    return render(request, 'pages/home.html', context)

def articles(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please login to see the articles page')
        return redirect('login')
    articles = Article.objects.all().order_by('-timestamp')
    context = {'articles': articles}
    return render(request, 'pages/articles.html', context)

def articles_ordered(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please login to see the articles page')
        return redirect('login')
    articles = Article.objects.all().order_by('-times_read')
    context = {'articles': articles}
    return render(request, 'pages/articles.html', context)

def article(request, id):
    if not request.user.is_authenticated:
        messages.info(request, ('Please login to see the article with ID: ' + str(id)))
        return redirect('login')
    article = Article.objects.get(id=id)
    article.times_read += 1
    article.save()
    context = {'article': article}
    return render(request, 'pages/article.html', context)

def breaking_news(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please login to see the breaking news')
        return redirect('login')
    articles = Article.objects.filter(breaking=True).order_by('-times_read')
    context = {'articles': articles}
    return render(request, 'pages/articles.html', context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username (or) Password is incorrect')

    context = {}
    return render(request, 'pages/login.html', context)

def logoutUser(request):
    if not request.user.is_authenticated:
        return redirect('home')
    messages.success(request, f'{request.user} has been succesfully logged out.')
    logout(request)
    return redirect('login')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterUserForm()
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account was created for {user}')
            return redirect('login')
        
    context = {'form': form}
    return render(request, 'pages/register.html', context)

def profile(request):
    if not request.user.is_authenticated:
        messages.info(request, 'Please login to view your profile')
        return redirect('login')
    context = {}
    return render(request, 'pages/profile.html', context)

def update_profile(request):
    if not request.user.is_authenticated:
        messages.info(request, 'You should be logged in to update your profile')
        return redirect('login')
    context = {}
    
    if request.method == "POST":
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account with username {request.user.username} has succesfully been updated!')
            return redirect('account')
    form = UserUpdateForm(instance=request.user)
    context = {'form': form}
    return render(request, 'pages/update_profile.html', context)