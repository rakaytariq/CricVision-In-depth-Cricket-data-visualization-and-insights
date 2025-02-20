from django.urls import path
#from . import views
from .views import HomeView, ArticleDetailView, AddPostView, edit_post, delete_post


urlpatterns = [
    #path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name='add-post'),
    path('post/edit/<int:pk>/', edit_post, name='edit-post'),
    path('post/delete/<int:pk>/', delete_post, name='delete-post'),
]
