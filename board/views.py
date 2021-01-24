from django.shortcuts import render
from .models import Board

# Create your views here.
def board_list(request):
    boards = Board.objects.all().order_by('id')  # -id: time 역순
    return render(request, 'board/bord_list.html', {'boards': boards})


# def write(request):
# return render(request, 'board/bord_list.html')
