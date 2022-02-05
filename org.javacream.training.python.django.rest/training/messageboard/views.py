from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'messageboard/index.html')
def board(request, board_name):
    return render(request, 'messageboard/board.html', {
      'board_name': board_name
    })
