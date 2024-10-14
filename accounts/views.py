from django.shortcuts import render, redirect
from django.http import  HttpResponse
from . import forms
from .forms import InputForm


# Create your views here.
def homepage(request):

    return render(request,"base.html")

def about_us(request):
    return HttpResponse("Hello, World. You're at the polls index")

def send(request):
    form = forms.InputForm()
    if request.method == "POST":
        form = forms.InputForm(request.POST)

    return render(request, "blog_entry.html",{'form':form})

def create_form(request):

    if request.method == "POST":
        form = forms.TopicForm(request.POST)

        if form.is_valid() :
            form.save()
            return redirect('first_app:article')
        else:
            print(form.errors)

    form = forms.TopicForm()
    return render(request,"blog_entry.html",{"form":form})

def create_form_one(request):

    if request.method == "POST":
        form = forms.ArticleForm(request.POST)

        if form.is_valid() :

            form.save()

        else:
            print(form.errors)

    form = forms.ArticleForm()
    return render(request,"blog_entry.html",{"form":form})

def create_form_two(request):

    if request.method == "POST":
        form = forms.CommentForm(request.POST)

        if form.is_valid() :
            form.save()

        else:
            print(form.errors)

    form = forms.CommentForm()
    return render(request,"blog_entry.html",{"form":form})