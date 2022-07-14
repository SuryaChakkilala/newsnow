from django.urls import path
from .views import home, articles, article, breaking_news, articles_ordered, loginPage, logoutUser, registerPage, profile, update_profile

urlpatterns = [
    path('', home, name='home'),
    path('articles', articles, name='articles'),
    path('articles/<id>', article, name='article'),
    path('breakingnews', breaking_news, name='breaking'),
    path('articlesordered', articles_ordered, name='articlesordered'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', registerPage, name='register'),
    path('profile', profile, name='profile'),
    path('updateprofile/', update_profile, name='updateprofile')
]