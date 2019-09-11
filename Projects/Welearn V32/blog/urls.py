from django.urls import path
from . import views

urlpatterns = [
    path('python-programing',views.FirtPost),
    path('python-examples',views.PythonExamples),
    path('python-examples/<int:id>/',views.ViewPost),
    path('test',views.Test),
    path('test2',views.Test2),
    path('CSharp',views.CSharp),
    path('CPP',views.CPP),
    path('Java',views.JAVA),
    path('PHP',views.PHP),
    path('ASP',views.ASP),
]
