from django.shortcuts import render, redirect, get_object_or_404
from . models import Meeting, Post, Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from . forms import TodoForm


def meeting(request):
    meetings = Meeting.objects
    return render(request, 'prodigies/home.html', {'meetings': meetings})


def post(request):
    posts = Post.objects
    return render(request, 'prodigies/post.html', {'posts': posts})


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


def todo(request):
    todos = Todo.objects.all().order_by('due_time')
    return render(request, 'prodigies/todo.html', {'todos': todos})


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
        if request.POST['post']:
            post = Post()
            post.post = request.POST['post']
            post.author = request.user
            post.save()
            # return redirect('/prodigies/'+str(meeting.id))
            return render(request, 'prodigies/post.html')

        else:
            return render(request, 'prodigies/create_post.html', {'error': 'All fields are required'})

    else:
        return render(request, 'prodigies/post.html')
