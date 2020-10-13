from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ToDoForm
from .models import ToDo
from django.utils import timezone
from django.contrib.auth.decorators import login_required

def signup_view(request):
	if request.method == 'GET':
		return render(request, 'signup.html', {'form' : UserCreationForm()})
	else:
		if (request.POST['password1'] == request.POST['password2']) and (request.POST['password1'] != ''):
			try:
				user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
				user.save()
				login(request, user)
				return redirect('home_view')
			except IntegrityError:
				return render(request, 'signup.html',
							 {'form' : UserCreationForm(),
				 			  'invalid' : 'Error: User name not available, please try again'})
		else:
			print('Error Code!')
			return render(request, 'signup.html',
			{'form' : UserCreationForm(),
			 'invalid' : 'Error: Password is corrupted, please try again'})

def login_view(request):
	if request.method == 'GET':
		return render(request, 'login.html', {'form' : AuthenticationForm()})
	else:
		user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
		if user is None:
			return render(request, 'login.html',
			 {'form' : AuthenticationForm(),
 			  'invalid' : 'Username and password don\'t match!'})
		else:
			login(request, user)
			return redirect('home_view')

@login_required
def logout_view(request):
	if request.method == 'POST':
		logout(request)
		return redirect('home_view')

@login_required
def todo_view(request, todo_pk):
	todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
	if request.method == "GET":
		form = ToDoForm(instance=todo)
		return render(request, 'todo.html', {'todo' : todo, 'form' : form})
	else:
		try:
			form = ToDoForm(request.POST, instance=todo)
			form.save()
			return redirect('home_view')
		except ValueError:
			return render(request, 'todo.html', {'todo' : todo,
												 'form' : form,
												 'invalid' : 'Data is corrupted!'} )

@login_required
def complete_view(request, todo_pk):
	todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
	if request.method == "POST":
		todo.complated_date = timezone.now()
		todo.save()
		return redirect('home_view')

@login_required
def delete_view(request, todo_pk):
	todo = get_object_or_404(ToDo, pk=todo_pk, user=request.user)
	if request.method == "POST":
		todo.delete()
		return redirect('home_view')

@login_required
def home_view(request):
	todos = ToDo.objects.filter(user=request.user, complated_date__isnull=True)
	return render(request, 'home.html', {'todos' : todos})

@login_required
def finished_view(request):
	todos = ToDo.objects.filter(user=request.user, complated_date__isnull=False).order_by('-complated_date')
	return render(request, 'finished.html', {'todos' : todos})

@login_required
def create_view(request):
	if request.method == "GET":
		return render(request, 'create.html',
			   {'form' : ToDoForm()})
	else:
		try:
			todo_form = ToDoForm(request.POST)
			new_todo = todo_form.save(commit=False)
			new_todo.user = request.user
			new_todo.save()
			return redirect('home_view')
		except ValueError:
			return render(request, 'create.html',
			 	   {'form' : ToDoForm(),
 			  	    'invalid' : 'Data is corrupted!'})

