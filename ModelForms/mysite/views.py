from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from mysite.forms import PostFrom
from mysite.models import Post
def list_posts(request):
    posts = Post.objects.all()
    return render(request, "list_posts.html", {'posts': posts})
def add_post (request):
    if request.method == "POST":
        form = PostFrom(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=True)
            model_instance.save()
            return redirect('list_posts')
        else:
            form = PostFrom()
            return render(request, "add_post.html", {'form': form})