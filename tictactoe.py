"""Tic Tac Toe."""

from turtle import *
from freegames import line


def grid():
    """Dibuja el tablero."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X."""
    color('blue')
    width(8)
    line(x + 25, y + 25, x + 108, y + 108)
    line(x + 25, y + 108, x + 108, y + 25)


def drawo(x, y):
    """Dibuja la O."""
    color('red')
    width(8)
    up()
    goto(x + 66.5, y + 66.5 - 42)
    down()
    circle(42)


def floor(value):
    """Redondea la coordenada al tablero."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = [None] * 9


def tap(x, y):
    """Maneja el clic en el tablero."""
    x = floor(x)
    y = floor(y)
    col = int((x + 200) // 133)
    row = int((y + 200) // 133)

    if col not in range(3) or row not in range(3):
        return

    index = row * 3 + col

    if board[index] is not None:
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[index] = player
    update()
    state['player'] = 1 - player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
