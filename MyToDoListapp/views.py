from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todolist
from .forms import Todolistform
# Create your views here.
def todolist(request):
    if request.method == "POST":
        todo = Todolistform(request.POST)
        if todo.is_valid():
            todo.save()
            return redirect('todolist')
    else:
        todo = Todolistform()
        data = Todolist.objects.all()
        return render(request,"todolist.html",{'todolist':todo,'data':data})

def delete(request,id):
    todo = Todolist.objects.get(id=id)
    todo.delete()
    return redirect('todolist')
