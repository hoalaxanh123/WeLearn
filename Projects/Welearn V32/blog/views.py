from django.shortcuts import render
from .models import *

# Create your views here.
def ListSubject(request):
    Data = {'Subjects':Subject.objects.all().order_by('-dateCreate')}
    return render(request,'learn/python.html',Data) 
def CSharp(request):
    return render(request,'learn/csharp.html') 
def CPP(request):
    return render(request,'learn/cpp.html') 
def JAVA(request):
    return render(request,'learn/java.html') 
def PHP(request):
    return render(request,'learn/PHP.html') 
def ASP(request):
    return render(request,'learn/ASP.html') 

def FirtPost(request):
    post = Post.objects.get(catID=1)
    return render(request,'learn/python.html',{'post':post}) 

def PythonExamples(request):
    lst = Post.objects.raw('SELECT * from blog_post where catID=2')
    return render(request,'learn/python-examples.html',{'lstPost':lst}) 

def ViewPost(request,id):
    post = Post.objects.get(id=id)
    return render(request,'learn/post.html',{'post':post})

def Test(request):
    menu = Category.objects.all()
    return render(request,'learn/test.html',{'menus':menu})

def Test2(request):
    subjects = Subject.objects.all()
    return render(request,'learn/test2.html',{'subjects':subjects})   
