from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('tryToLogin', views.tryToLogin),
    path('subDetail/id=<int:id>', views.subDetail),
    path('userDetail/id=<int:id>', views.userDetail),
    path('subDelete/id=<int:id>', views.DeleteSubject),
    path('UpdateSubject', views.UpdateSubject),
    path('UpdateUser', views.UpdateUser),
    path('AddSubject', views.AddSubject),
    path('AddUser', views.AddUser),
    path('AddCategory', views.AddCat),
    path('AddPost', views.AddPost),
    path('CreateSubject', views.subDetailNull),
    path('CreateUser', views.userDetailNull),
    path('CreateCategory', views.catDetailNull),
    path('CreatePost', views.postDetailNull),
    path('subjects', views.subjects),
    path('users', views.users),
    path('categories', views.categories),
    path('posts', views.posts),
    path('catDelete/id=<int:id>', views.DeleteCat),
    path('userDelete/id=<int:id>', views.DeleteUser),
    path('postDelete/id=<int:id>', views.DeletePost),
    path('catDetail/id=<int:id>', views.catDetail),
    path('PostDetail/id=<int:id>', views.postDetail),
    path('UpdatePost', views.UpdatePost),
    path('UpdateCat', views.UpdateCat),
    path('login', views.login)
]
