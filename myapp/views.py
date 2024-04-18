from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,JsonResponse
from .models import project,Task
from .forms import CreateNewTask ,CreateNewProject
# Create your views here.
def index(request):
    title='Django course!'
    return render(request,'index.html',{
        'title':title
    })

def about(request):
    return render(request,'about.html')

def hello(request,username):
    
    return HttpResponse('<h1>hola mundo vamos no joda %s</h1'% username)

def projects(request):
    #projec=list(project.objects.values())
    projects=project.objects.all()
    return render(request,'projects.html',{
        'projects':projects
    })

def tasks(request):
    #task=Task.objects.get(id=id)
    #return HttpResponse('tasks: %s'% task.title)
    tasks=Task.objects.all()
    return render(request,'tasks.html',{
        'tasks':tasks
    })
    
def create_new_task(request):
    if request.method=='GET':
        return render(request,'create_task.html',{
        'form': CreateNewTask()
        }) 
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'],project_id=1)    
        return redirect('tasks')
    
def create_new_project(request):
    if request.method=='GET':
        return render(request,'create_project.html',{
        'form': CreateNewProject()
        }) 
    else:
         project.objects.create(name=request.POST['name'])
         return redirect('projects')
         
def  project_detail(request,id):
     p=project.objects.get(id=id)
     get_object_or_404(project,id=id)
     t=Task.objects.filter(project_id=id)
     return  render(request, 'detail.html',{
         'project':p,
         'tasks':t
     })      
         
    
       
    
