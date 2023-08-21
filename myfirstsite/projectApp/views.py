from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoList,Item
from .forms import CreateNewList
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def first(Response):
    return render(Response,"main/index.html",{})

def index(Response,id):
    ls = ToDoList.objects.get(id=id)
    if Response.method == "POST":
        if Response.POST.get("save"):
            for item in ls.item_set.all():
                if Response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        elif Response.POST.get("newItem"):
            txt = Response.POST.get("new")
            if len(txt) > 2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("invalid")
    return render(Response,"main/view.html",{"ls":ls})
    

def create(Response):
    if Response.method == "POST":
        form = CreateNewList(Response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            Response.user.todolist.add(t)
        return HttpResponseRedirect("/%i" %t.id)        
    else:
        form = CreateNewList()
    return render(Response,"main/create.html",{"form":form})

def view(response):
    return render(response, "main/viewLists.html", {})

def base(response):
    return render(response,"main/base.html",{})

