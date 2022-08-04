from django.contrib import messages
from django.shortcuts import render, redirect

from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import teamdetail, testimonyp, Post
from .forms import CONTACTFORM, CommentForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic


def index(request):
    return render(request, "mainweb/index.html")
def main(request):
    return render(request, "main.html")
class BlogView(generic.ListView):
    template_name ='mainweb/blog.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:10]


def blogdetail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('blogdetail', slug=post.slug)
    else:
        form = CommentForm()

    context ={'post' : post, 'form':form}
    return render(request, "mainweb/blog-single.html", context)


def contact(request):
    form = CONTACTFORM()
    if request.method =='POST':
        form = CONTACTFORM(request.POST, request.FILES )
        if form.is_valid():
            #form= form.save(commit=False)
            form.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('contact')


    return render(request, "mainweb/contact.html", {'form':form})
def service(request):
    return render(request, "mainweb/services.html")
class TeamView(generic.ListView):
    template_name = 'mainweb/team.html'
    context_object_name = 'teams'
    def get_queryset(self):
        return teamdetail.objects.order_by('-created')
def about(request):
    return render(request, "mainweb/about.html")
class TestimonyView(generic.ListView):
    template_name = 'mainweb/testimonials.html'
    context_object_name= 'texty'
    def get_queryset(self):
        return testimonyp.objects.order_by('-created')
class RecentpostView(generic.ListView):
    template_name='mainweb/recentpost.html'
    context_object_name = 'posts'
    def get_queryset(self):
        return Post.objects.order_by('-date_added')[:6]
"""
from django.db.models import Q
import requests
from django.shortcuts import render, redirect
from .models import teamdetail, testimonyp, Post
from .forms import CONTACTFORM, CommentForm
from django.http import HttpResponse
# Create your views here.
from django.contrib import messages

def index(request):
    return render(request, "mainweb/index.html")


def contact(request):
    form = CONTACTFORM()
    if request.method =='POST':
        form = CONTACTFORM(request.POST, request.FILES )
        if form.is_valid():
            #form= form.save(commit=False)
            form.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('contact')


    return render(request, "mainweb/contact.html", {'form':form})

def service(request):
    return render(request, "mainweb/services.html")
def team(request):
    teams = teamdetail.objects.order_by('created')
    context = {'teams' : teams}

    return render(request, "mainweb/team.html", context)
def blogdetail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method =='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            messages.success(request, ('thank for contact us'))
        else:
            messages.error(request, ' an error occur in the submitions ')
        return redirect('blogdetail', slug=post.slug)
    else:
        form = CommentForm()

    context ={'post' : post, 'form':form}
    return render(request, "mainweb/blog-single.html", context)
def blog(request):
    posts= Post.objects.order_by('date_added')
    context ={'posts' : posts}
    return render(request, "mainweb/blog.html", context)
def testimony(request):
    texty= testimonyp.objects.order_by('created')
    context = {'texty':texty}
    return render(request, "mainweb/testimonials.html", context)
def main(request):

    return render(request, "main.html")
def about(request):
    return render(request, "mainweb/about.html")

def recentpost(request):
    posts= Post.objects.order_by('date_added')
    context ={'posts' : posts, 'Comment_count':Comment_count}
    return render(request, "mainweb/recentpost.html")
"""