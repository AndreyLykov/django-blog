from django.shortcuts import render, get_object_or_404
from models import BlogPost, Comment
from forms import BlogPostForm, AddCommentForm
from django.http import redirect, reverse, Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    posts = BlogPost.objects.all()
    context = {"posts": posts}
    return render(request, 'index.html', context)

def post(request, post_id):
    current_post = BlogPost.objects.get(pk=post_id)
    context = {"current_post": current_post}
    return render(request, 'post_details.html', context)

@login_required
def add_post(request, post_id):
    if request.method == 'POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post.save()
            return redirect(reverse('post_details.html', kwargs={'post_id': post.pk}))
        else:
            form = BlogPost()
            
        return render(request, 'create_post.html', {'post': post})
    
@login_required
def add_comment(request, post_id):
    form = AddCommentForm(request.POST)
    if form.is_valid():
        form.save(commit=False)
        Comment.post = BlogPost(post_id=post.pk)
        Comment.author = request.user
        form.save()
        
        return redirect(reverse('post_details.html', kwargs={'post_id': post.pk}))

@login_required
def edit_post(request, post_id):   
    current_post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == "POST":
        current_post = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save(commit=False)
            current_post.author = request.user
            form.save()
            redirect('post_details.html', post_id=post.pk)
        else:
            form = BlogPost(instance=post)
        
        context = {'post': post, 'form': form}    
        return render(request, 'edit_post.html', context)

def check_post_author(request, User):
    if BlogPost.author != User:
        raise Http404