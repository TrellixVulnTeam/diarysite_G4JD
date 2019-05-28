
from django.shortcuts import render,redirect, get_object_or_404
from .models import Blog 
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import datetime
from .forms import BlogForm 
from django.contrib.auth.models import User
from django.contrib import auth


def lists(request):
    blog = Blog.objects.all()
    blog_list = Blog.objects.all()
    paginator = Paginator(blog_list, 4)
    page = request.GET.get('page')
    
    try: 
        posts = paginator.get_page(page)
    except PageNotAnInteger:
        posts = page.get_page(1)
    except EmptyPage :
        posts = paginator.get_page(paginator.num_pages)

    return render(request, 'lists.html', {'blog' : blog, 'posts' : posts})

def new(request):
   
    if request.method == 'GET':
        form = BlogForm() 
        return render(request, 'new.html', {'form':form})

    else:
        form = BlogForm(request.POST)

        if form.is_valid(): 
            blog = form.save(commit = False)
            blog.date = timezone.now()
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            blog.image = fs.url(filename)
            blog.user = request.user.username
            blog.save()
            return redirect('/'+ str(blog.id) ) 
        return redirect('/') 

def create(request):
    blog = Blog()
    blog.title = request.POST['title']
    blog.description = request.POST['description']
    blog.date = timezone.datetime.now()
   
    if request.method == 'POST'and request.FILES['image']:
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        blog.image = fs.url(filename)
    blog.save()
    return redirect('/')
   

def detail(request, blog_id):
    blog = Blog.objects.get(pk = blog_id) # pk에 조건 여러가지 걸수 있음 #

    return render(request, 'detail.html', {'blog': blog})

def edit(request, blog_id):

    blog = get_object_or_404(Blog, pk = blog_id )
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.description = request.POST['description']
        blog.user = request.user.username
        if request.FILES['image']:
            myfile = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            blog.image = fs.url(filename)
        blog.save()

        return redirect('/')
    else:
        return render(request, 'edit.html', {'blog' : blog})

def delete(request, blog_id):
    blog = get_object_or_404(Blog, pk = blog_id)
    blog.delete()

    return redirect('/')
    


def signup(request):
    if request.method == 'POST':

        if request.POST['username'] == '' or request.POST['password'] == '':
            return render(request, 'signup.html', {'error':'아이디 비밀번호 필수 입력'})
        if request.POST['password'] != request.POST['con_password']:
            return render(request, 'signup.html', {'error':'비밀번호 불일치'})
        try :
            user = User.objects.get(username = request.POST['username'])
            return render(request, 'signup.html', {'error':'이미 존재하는 아이디'})
        
        except User.DoesNotExist:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password'])
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST' :
        username = request.POST['username']
        pw = request.POST['password']

        user = auth.authenticate(request, username = username, password = pw)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error':'아이디 비밀번호 확인'})

    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

