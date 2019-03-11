from django.shortcuts import render, redirect
from .models import Board #### . 조심
import requests

# Create your views here.
def index(request):
    # return render(request, 'index.html')
    boards = Board.objects.all()
    # boards = Board.objects.get.ordered_by('-id')
    # titles = request.POST.get('title')
    # contents = request.POST.get('content')
    return render(request, 'boards/index.html', {'boards' : boards})
    # return render(request, 'boards/index.html', { 'titles' : titles , 'contents' : contents})
    
def new(request):
    return render(request, 'new.html')
    
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    created_at = request.POST.get('created_at')
    updated_at = request.POST.get('updated_at')
    return render(request, 'boards/detail.html', {'title' : title, 'content' : content, 'created_at' : created_at, 'updated_at' : updated_at})
 
def detail(request, pk): 
    board = Board.objects.get(pk = pk)
    return render(request, 'boards/detail.html', {'board' : board})
    # title = request.POST.get('title')
    # content = request.POST.get('content')
    # created_at = request.POST.get('created_at')
    # updated_at = request.POST.get('updated_at')
    # return render(request, 'detail.html', {'title' : title, 'content' : content, 'created_at' : created_at, 'updated_at' : updated_at})
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    board.delete()
    return redirect('/boards')
    
def edit(request, pk):
    board = Board.objects.get(pk = pk)
    return render(request, 'boards/edit.html', {'board' : board})

def update(request, pk):
    board = Board.objects.get(pk = pk)
    return render(request, 'boards/update.html', {'board' : board})