from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Students
from .forms import StudentsForm

def index(request):

    return render(request,'core/index.html',{'student':Students.objects.all()})

def detail(request,id):
    person = Students.objects.get(pk=id)
    return render(request,'core/detail.html',{'student':person})

def add(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'core/add.html',{'form':StudentsForm()})

def edit(request,id):
    if request.method == 'POST':
        person = Students.objects.get(pk=id)
        form = StudentsForm(request.POST,instance=person)
        if form.is_valid():
            form.save()
            return render(request,'core/edit.html',{'form':form})
    else:
        person = Students.objects.get(pk=id)
        form = StudentsForm(instance=person)
    return render(request,'core/edit.html',{'form':form})

def delete(request,id):
    if request.method == 'POST':
        person = Students.objects.get(pk=id)
        person.delete()
    return HttpResponseRedirect(reverse('index'))
