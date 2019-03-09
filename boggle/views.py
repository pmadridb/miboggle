from django.shortcuts import render
from django.http import HttpResponse
import random

def index(request):
    cubes = ["EEGUMA",
        "ESPTCI",
        "ARISYF",
        "LITCEP",
        "AEDNNN",
        "PYIFRS",
        "OOÑTNU",
        "JKBXZQ",
        "RRYRIP",
        "TETIII",
        "HDROLN",
        "SUSENS",
        "RDHOHL",
        "RFSAAA",
        "TOUOTO",
        "MTTTEO",
        "GRRVÑO",
        "CSNTEC",
        "SARIFA",
        "DTNODH",
        "EEEEMA",
        "LDNORH",
        "EEEEAA",
        "MGNAEN",
        "TELIIC"]
    w, h = 5, 5;
    board = [[0 for x in range(w)] for y in range(h)]
    index = 0
    for i in range(w):
        for j in range(h):
            board[i][j] = cubes[index][random.randint(0,5)]
            if board[i][j] == 'Q':
                board[i][j] = 'Qu'
            index += 1
    context = {'board': board}
    return render(request, 'index.html', context)