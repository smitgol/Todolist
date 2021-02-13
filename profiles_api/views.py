from django.shortcuts import render, redirect
from .models import *
from .forms import *
from . import serializers
from . import permissions


from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.settings import api_settings
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import filters
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    tasks = List.objects.filter(user=request.user)
    print(tasks)
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)
            q.user = request.user
            q.save()
            
        return redirect('list')
    context = {
        'tasks': tasks,
        'form': form
    }
    return render(request, 'index.html', context)
@login_required
def updateTask(request, pk):
	task = List.objects.get(id=pk)

	form = TaskForm(instance=task)
	if request.method == 'POST':
		form = TaskForm(request.POST, instance=task)
		if form.is_valid():
			form.save()
			return redirect('list')

	context = {'form':form}

	return render(request, 'update_task.html', context)
@login_required
def deleteTask(request, pk):
	item = List.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('list')

	context = {'item':item}
	return render(request, 'delete.html', context)
    
class TodolistViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TodolistSerializer
    queryset = List.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('task', 'id')

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email')

class UserLoginApiView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


#@api_view(['GET', 'POST'])
#def todo_list(request):
#    if request.method == "GET":
#        todo = List.objects.all()
#        serializer = serializers.TodolistSerializer(todo, many=True)
#        return Response(serializer.data)
