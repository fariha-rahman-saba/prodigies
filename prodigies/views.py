from django.shortcuts import render, redirect, get_object_or_404
from . models import Post, Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . forms import TodoForm, PostForm

def post(request):
    posts = Post.objects.order_by('-created')
    return render(request, 'prodigies/post.html', {'posts': posts})


@login_required
def myposts(request):
    posts = Post.objects.filter(user=request.user).order_by('-created')
    return render(request, 'prodigies/myposts.html', {'posts': posts})

@login_required
def mytodos(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created')
    return render(request, 'prodigies/mytodo.html', {'todos': todos})



def todo(request):
    todos = Todo.objects.all().order_by('due_time')
    return render(request, 'prodigies/todo.html', {'todos': todos})


@login_required
def todo_ud(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    if request.method == "GET":
        form = TodoForm(instance=todo)
        return render(request, 'prodigies/edit_todo.html', {'todo': todo, 'form': form})
    else:
        form = TodoForm(request.POST, instance=todo)
        form.save()
        return redirect('todo')


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        newpost = form.save(commit=False)
        newpost.user = request.user
        newpost.save()
        return redirect('post')

    else:
        return render(request, 'prodigies/create_post.html')


@login_required
def create_todo(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        newtodo = form.save(commit=False)
        newtodo.user = request.user
        newtodo.save()
        return redirect('todo')

    else:
        return render(request, 'prodigies/create_todo.html', {'form': TodoForm()})

@login_required
def post_ud(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        form = PostForm(instance=post)
        return render(request, 'prodigies/edit_post.html', {'post': post, 'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        form.save()
        return redirect('post')


@login_required
def delete_post(request,post_id):
    post_to_delete=Post.objects.get(pk=post_id)
    post_to_delete.delete()
    return redirect('myposts')

@login_required
def delete_todo(request,todo_id):
    todo_to_delete=Todo.objects.get(pk=todo_id)
    todo_to_delete.delete()
    return redirect('mytodos')