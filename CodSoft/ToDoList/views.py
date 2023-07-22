from django.shortcuts import render,redirect
from .models import taskList

def index(request):
    return render(request,'index.html')


def todolist(request):  
    if request.POST:
        task = request.POST['additem']
        taskList(task=task).save()
        print("success")
    obj = taskList.objects.all().order_by('-id')
    return render(request,'todolist.html',{'list':obj})

def updateItem(request,id):
    if request.POST:
        temToUpdate = taskList.objects.get(pk=id)
        task = request.POST['additem']
        temToUpdate.task = task
        temToUpdate.save()
        return redirect(todolist)

    utask=taskList.objects.get(id=id).task
    obj = taskList.objects.all().order_by('-id')
    return render(request,'todolist.html',{'list':obj,'utask':utask})

def deleteItem(request,id):
    itemToDelete = taskList.objects.get(pk=id)
    itemToDelete.delete()
    return redirect(todolist)


    

