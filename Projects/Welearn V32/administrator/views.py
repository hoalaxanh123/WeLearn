from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from blog.models import *
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import redirect


# Create your views here.


def index(request):
    return render(request, 'pages/index.html')


def login(request):
    return render(request, 'pages/login.html')


def IsLogged():
    user = request.session['admin']
    if user != "":
        return True
    else:
        del request.session['admin']
        return False


@csrf_exempt
def tryToLogin(request):
    try:
        userName = str(request.POST.get("usr"))
        rs = HttpResponse()
        passWord = str(request.POST.get("pass"))
        # rs.write(userName+passWord)
        user = User.objects.get(username=userName, password=passWord)
        request.session['admin'] = user.username
        rs.write("Đăng nhập thành công")
    except Exception as e:
        rs.write(e)
        rs.write("Sai tên tài khoản hoặc mật khẩu , vui lòng kiểm tra lại")
    return rs


@csrf_exempt
def UpdateSubject(request):
    ID = int(request.POST.get("id"))
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    date = str(request.POST.get("datecreate"))
    logo = str(request.POST.get("logo"))
    thumbnail = str(request.POST.get("thumbnail"))
    shortName = str(request.POST.get("shortname"))
    Subject.objects.filter(pk=ID).update(title=title, shortName=shortName, description=des,
                                         dateCreate=datetime.datetime.now(), thumbail=thumbnail, logo=logo)
    subjects = Subject.objects.all()
    return redirect('/manage/subjects')


@csrf_exempt
def AddSubject(request):
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    date = str(request.POST.get("datecreate"))
    logo = str(request.POST.get("logo"))
    thumbnail = str(request.POST.get("thumbnail"))
    shortName = str(request.POST.get("shortname"))
    sub = Subject(title=title, shortName=shortName, description=des,
                  dateCreate=datetime.datetime.now(), thumbail=thumbnail, logo=logo)
    sub.save()
    return redirect('/manage/subjects')


@csrf_exempt
def AddCat(request):
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    SubID = int(request.POST.get("SubID"))
    cat = Category(title=title, description=des, subjectID=SubID)
    cat.save()
    return redirect('/manage/categories')


@csrf_exempt
def DeleteSubject(request, id):
    Subject.objects.filter(pk=id).delete()
    return redirect('/manage/subjects')


@csrf_exempt
def DeleteUser(request, id):
    User.objects.filter(pk=id).delete()
    return redirect('/manage/users')


@csrf_exempt
def UpdateCat(request):
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    ID = int(request.POST.get("id"))
    SubID = int(request.POST.get("SubID"))
    Category.objects.filter(pk=ID).update(
        title=title, description=des, id=ID, subjectID=SubID)
    return redirect('/manage/categories')


@csrf_exempt
def UpdateUser(request):
    ID = int(request.POST.get("userID"))
    Role = int(request.POST.get("role"))
    User.objects.filter(pk=ID).update(
        role=Role)
    return redirect('/manage/users')


@csrf_exempt
def UpdatePost(request):
    catID1 = int(request.POST.get("CatID"))
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    contents = str(request.POST.get("content"))
    author = str(request.POST.get("author"))
    ID = int(request.POST.get("id"))
    Post.objects.filter(pk=ID).update(
        title=title, description=des, catID=catID1, content=contents, creator=author)
    return redirect('/manage/posts')


@csrf_exempt
def AddPost(request):
    catID1 = int(request.POST.get("CatID"))
    title = str(request.POST.get("title"))
    des = str(request.POST.get("descripton"))
    contents = str(request.POST.get("content"))
    author = str("root")  # Trường này sẽ lấy từ session ( về sau sửa )
    date = datetime.datetime.now()
    post = Post(
        title=title, description=des, catID=catID1, content=contents, creator=author, dateCreate=date)
    post.save()
    return redirect('/manage/posts')


@csrf_exempt
def AddUser(request):
    RealName = str(request.POST.get("realname"))
    Pass = str(request.POST.get("pass1"))
    UserName = str(request.POST.get("username"))
    Email = str(request.POST.get("email"))
    Role = int(request.POST.get("role"))
    user = User(username=UserName, password=Pass,
                realname=RealName, email=Email, role=Role)
    user.save()
    return redirect('/manage/users')


@csrf_exempt
def DeletePost(request, id):
    Post.objects.filter(pk=id).delete()
    return redirect('/manage/posts')


@csrf_exempt
def DeleteCat(request, id):
    Category.objects.filter(pk=id).delete()
    return redirect('/manage/categories')


def subjects(request):
    subjects = Subject.objects.all()
    return render(request, 'pages/subjects.html', {'subjects': subjects})


def subDetail(request, id):
    subject = Subject.objects.get(id=id)
    return render(request, 'pages/subDetail.html', {'subject': subject})


def userDetail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'pages/userDetail.html', {'user': user})


def postDetail(request, id):
    lst_cat = Category.objects.all()
    post = Post.objects.get(id=id)
    return render(request, 'pages/postDetail.html', {'post': post, 'lst_cat': lst_cat})


def subDetailNull(request):
    return render(request, 'pages/subAdd.html')


def userDetailNull(request):
    return render(request, 'pages/userAdd.html')


def postDetailNull(request):
    lst_Category = Category.objects.all()
    return render(request, 'pages/postAdd.html', {'lst_cat': lst_Category})


def users(request):
    lst_user = User.objects.all()
    return render(request, 'pages/users.html', {'lst_user': lst_user})


def categories(request):
    lst_cat = Category.objects.all()
    subjects = Subject.objects.all()
    return render(request, 'pages/categories.html', {'lst_cat': lst_cat, 'lst_sub': subjects})


def catDetailNull(request):
    subjects = Subject.objects.all()
    return render(request, 'pages/catADD.html', {'subjects': subjects})


def catDetail(request, id):
    subjects = Subject.objects.all()
    category = Category.objects.get(id=id)
    return render(request, 'pages/catDetail.html', {'category': category, 'subjects': subjects})


def posts(request):
    lst_post = Post.objects.all()
    lst_cat = Category.objects.all()
    return render(request, 'pages/posts.html', {'lst_post': lst_post, 'lst_cat': lst_cat})
