from django.urls import path
from app import views
from . import views


urlpatterns = [
    path('Login', views.handleLogin, name='login'),
    path('Signup', views.handleSignup, name='Signup'),
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('player-analysis', views.player_analysis, name='player-analysis'),
    path('shot_selection', views.shot_selection, name='shot_selection'),
    path('trend_analysis', views.trend_analysis, name='trend_analysis'),
    path('Logout', views.handleLogout, name='Logout'),
    path('team_and_player', views.team_and_player, name='team_and_player'),
    path('forum/', views.forum, name='forum'),
    path('newsandletter', views.newsandletter, name='newsandletter'),
 
]
