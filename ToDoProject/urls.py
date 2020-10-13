"""ToDoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from toDoData.views import signup_view
from toDoData.views import home_view
from toDoData.views import todo_view
from toDoData.views import logout_view
from toDoData.views import login_view
from toDoData.views import create_view
from toDoData.views import complete_view
from toDoData.views import delete_view
from toDoData.views import finished_view

urlpatterns = [
    path('admin/', admin.site.urls),

    #auth
    path('signup/', signup_view, name='signup_view'),
    path('logout/', logout_view, name='logout_view'),
    path('login/', login_view, name='login_view'),
    #todo
    path('home/', home_view, name='home_view'),
    path('home/finished', finished_view, name='finished_view'),
    path('home/<int:todo_pk>', todo_view, name='todo_view'),
    path('home/<int:todo_pk>/complete', complete_view, name='complete_view'),
    path('home/<int:todo_pk>/delete', delete_view, name='delete_view'),
    path('todo_create/', create_view, name='create_view'),
]
