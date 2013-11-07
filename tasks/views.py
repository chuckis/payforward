from django.shortcuts import render, render_to_response, redirect
from tasks.models import *
from forms import *
from django.core.context_processors import csrf
from django.template import RequestContext
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
#import random
from crispy_forms.utils import render_crispy_form #?
from thumbs import generate_thumb


def index(request):
    tasks = Task.objects.all()
    important_tasks = tasks.order_by('-rate')[0:4]
    fresh_tasks = tasks.order_by('-create_date')[0:4]
    form = CreateTaskForm()
    return render_to_response('index.html',{'important_tasks':important_tasks,'fresh_tasks':fresh_tasks, 'form':form}, context_instance=RequestContext(request))
    
def login_user(request):
    logout(request)
    username=password=''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
            return redirect('/register')
    return render_to_response('login.html', context_instance=RequestContext(request))


@login_required(login_url='/login/')  
def create_task(request):
    if request.method == 'POST':
        form = CreateTaskForm(request.POST, request.FILES,)
        if form.is_valid():
            task = form.save(commit=False) #commit=False
            if not task.task_photo:
                number = random.randint(1,6)
                task.task_photo = 'task_photos/page4-img'+str(number)+'.jpg'
            task.user = request.user
            task.save()
            return redirect('/task/'+str(task.id))
    return redirect('/')


def tasks(request):
    tasks = Task.objects.all()
    return render_to_response('tasks.html',{'tasks':tasks}, context_instance=RequestContext(request)) #

def task(request,task_id):
    task = Task.objects.get(id=task_id)
    tasks = Task.objects.exclude(id=task_id)[0:4]
    return render_to_response('task.html',{'task':task, 'tasks':tasks}, context_instance=RequestContext(request))
    

def profile(request,user_id):
    return render_to_response('profile.html')

def people(request):
    people = Profile.objects.all()
    return render_to_response('people.html', {'people': people}, context_instance=RequestContext(request))
    
def register(request):
    if request.method == 'POST':
            form = UserCreationForm(request.POST)
            if form.is_valid():
                new_user = form.save()
                return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render( request, "register.html", {'form': form,})
    
def log_out(request):
    logout(request)
    return index(request)
    
    
