from django.shortcuts import render

from .models import Post
# Create your views here.
# from django.http import HttpResponse

def home(request):
    return render(request,'page/home.html')

def about(request):
    posts = Post.objects.all().order_by('-id')
    context = {
        'posts':posts
    }
    return render(request,'page/about.html',context)


def course(request):
    courses = Post.objects.all().order_by('-id')

    context = {
        'courses': courses
    }

    return render(request, 'page/course.html', context)


def blog(request):
    return render(request,'page/blog.html')

def contact(request):
    return render(request,'page/contact.html')


def postdetail(request,id):
    postdetails = Post.objects.get(id = id)
    context = {
            'postdetails':postdetails
        }
    return render(request,'page/postdetail.html',context)