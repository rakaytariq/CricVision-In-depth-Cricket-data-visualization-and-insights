from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from forum.models import Post
from .forms import PostForm
from django.shortcuts import render, get_object_or_404, redirect
from .forms import EditPostForm
from django.http import HttpResponseRedirect



#def home(request):
#   return render(request, 'home.html', {})
class HomeView(ListView):
    model= Post
    template_name = 'home.html'

class ArticleDetailView(DetailView):
    model= Post
    template_name ='article_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'



class UpdatePostView(UpdateView):
    model= Post
    fields =["title", "title_tag", "body"]
    template_name = 'add_post.html'

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = EditPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home') 
        login_url = '/login/' # Replace with the name of the view to redirect after editing
    else:
        form = EditPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post.delete()
        return HttpResponseRedirect('/home/')  # Redirect to a URL after deletion
    return render(request, 'delete_post.html', {'post': post})

