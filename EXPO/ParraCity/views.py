from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm, User_form
from django.shortcuts import redirect
from django.views.generic import FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('ParraCity.views.post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'ParraCity/post_edit.html', {'form': form})

def home(request):
    posts = Post.objects.filter(creacion__lte=timezone.now()).order_by('creacion')
    return render (request, 'ParraCity/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.order_by('categoria_post')
    return render (request, 'ParraCity/postlist.html', {'posts': posts})

def post_detail(request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'ParraCity/post_detail.html', {'post': post})

@login_required
def post_new(request):
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.autor = request.user
                post.publicacion = timezone.now()
                post.save()
                return redirect('ParraCity.views.post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'ParraCity/post_edit.html', {'form': form})

class signup(FormView):
    template_name = 'ParraCity/Signup.html'
    form_class = User_form
    success_url = reverse_lazy('home_view')

    def form_valid(self, form):
        form.save()
        return super(signup, self).form_valid(form)

def delete_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_ipk = post.pk
    post.delete()
    return render(request, "ParraCity/home.html")
