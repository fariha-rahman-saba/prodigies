from django.shortcuts import render
from . models import Meeting, Post, Todo
from django.contrib.auth.decorators import login_required
from django.utils import timezone


def meeting(request):
    meetings = Meeting.objects
    return render(request, 'prodigies/home.html', {'meetings': meetings})


def todo(request):
    todos = Todo.objects.all().order_by('due_time')
    return render(request, 'prodigies/todo.html', {'todos': todos})


def post(request):
    posts = Post.objects
    return render(request, 'prodigies/post.html', {'posts': posts})


@login_required(login_url="/accounts/signup/")
def create_class(request):
    if request.method == 'POST':
        if request.POST['class_title'] and request.POST['date'] and request.POST['time'] and request.POST['url']:
            meeting = Meeting()
            meeting.title = request.POST['class_title']
            meeting.date = request.POST['date']
            meeting.time = request.POST['time']
            meeting.url = request.POST['url']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                meeting.url = request.POST['url']
            else:
                meeting.url = 'http://' + request.POST['url']

            meeting.created = timezone.datetime.now()
            meeting.author = request.user
            meeting.save()
            # return redirect('/prodigies/'+str(meeting.id))
            return render(request, 'prodigies/create_class.html')

        else:
            return render(request, 'prodigies/create_class.html', {'error': 'All fields are required'})

    else:
        return render(request, 'prodigies/create_class.html')


@login_required(login_url="/accounts/signup/")
def create_todo(request):
    if request.method == 'POST':
        if request.POST['todo_title'] and request.POST['desc'] and request.POST['due_time']:
            todo = Todo()
            todo.title = request.POST['todo_title']
            todo.desc = request.POST['desc']
            todo.due_time = request.POST['due_time']
            todo.author = request.user
            todo.created = timezone.datetime.now()
            todo.save()
            # return redirect('/prodigies/'+str(meeting.id))
            return render(request, 'prodigies/create_todo.html')

        else:
            return render(request, 'prodigies/create_todo.html', {'error': 'All fields are required'})

    else:
        return render(request, 'prodigies/create_todo.html')


@login_required(login_url="/accounts/signup/")
def create_post(request):
    if request.method == 'POST':
        if request.POST['post']:
            post = Post()
            post.post = request.POST['post']
            post.created = timezone.datetime.now()
            post.author = request.user
            post.save()
            # return redirect('/prodigies/'+str(meeting.id))
            return render(request, 'prodigies/create_post.html')

        else:
            return render(request, 'prodigies/create_post.html', {'error': 'All fields are required'})

    else:
        return render(request, 'prodigies/create_post.html')
