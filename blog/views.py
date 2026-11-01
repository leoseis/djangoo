from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

def home(request):
        posts = Post.objects.order_by('-created_at')
        return render(request, 'blog/home.html', {'posts': posts})
def about(request):
        return render(request, 'blog/about.html')



from .forms import PostForm

def post_create(request):
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            form = PostForm()

        return render(request, 'blog/post_form.html', {
            'form': form,
            'page_title': 'Create a Blog Post',
        })



def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})






def post_update(request, pk):
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)

        return render(request, 'blog/post_form.html', {
            'form': form,
            'page_title': 'Edit Blog Post',
        })


def post_delete(request, pk):
        post = get_object_or_404(Post, pk=pk)

        if request.method == 'POST':
            post.delete()
            return redirect('home')

        return render(request, 'blog/post_confirm_delete.html', {'post': post})

