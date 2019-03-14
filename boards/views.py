from django.shortcuts import render, redirect
from .models import Board
from pprint import pprint   # 터미널에서 볼 때 사용

# Create your views here.
def index(request):
    pprint(request)
    pprint(type(request))
    pprint(dir(request))
    pprint(request.scheme)
    pprint(request.get_host())
    pprint(request.get_full_path())
    pprint(request.build_absolute_uri())
    pprint(request.META)
    pprint(request.method)
    
    boards = Board.objects.order_by('-pk')
    context = {  # context를 통해 딕셔너리를 html에 넣음
        'boards': boards,
    }
    return render(request, 'boards/index.html', context)
    
def new(request):  # 함수가 하나 줄어들고 restful하게 바뀜
    if request.method == 'POST':
        # CREATE
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        board = Board(title=title, content=content)
        board.save()
        return redirect('boards:detail', board.pk)
    else:   
        return render(request, 'boards/new.html')
    
# def create(request):
#     title = request.POST.get('title')
#     content = request.POST.get('content')
    
#     board = Board(title=title, content=content)
#     board.save()
#     # return redirect(f'/boards/{ board.pk }/')
#     return redirect('boards:detail', board.pk)
    
def detail(request, pk):
    board = Board.objects.get(pk=pk)
    context = {
        'board': board,
    }
    return render(request, 'boards/detail.html', context)
    
def delete(request, pk):
    board = Board.objects.get(pk=pk)
    if request.method == "POST":
        board.delete()
        # return redirect('/boards/')
        return redirect('boards:index')
    else:  # 주소로 입력하면 detail 페이지가 보이도록 함
        return redirect('boards:detail', board.pk)
    
def edit(request, pk):
    board = Board.objects.get(pk=pk)
    
    if request.method == "POST":  # UPDATE
        board.title = request.POST.get('title')
        board.content = request.POST.get('content')
        board.save()
        return redirect('boards:detail', board.pk)
    else:   # EDIT
        context = {
            'board': board,
        }
        return render(request, 'boards/edit.html', context)

# def update(request, pk):
#     board = Board.objects.get(pk=pk)
#     board.title = request.POST.get('title')
#     board.content = request.POST.get('content')
#     board.save()
#     # return redirect(f'/boards/{ board.pk }/')
#     return redirect('boards:detail', board.pk)
    