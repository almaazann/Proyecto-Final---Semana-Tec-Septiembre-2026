"""Tic Tac Toe."""

from turtle import *
from freegames import line

WINS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]


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


def winner():
    """Revisa si alguien ganó."""
    for a, b, c in WINS:
        if board[a] is not None and board[a] == board[b] == board[c]:
            return board[a]
    return None


def show_message(text):
    """Muestra un mensaje al terminar la partida."""
    up()
    goto(-120, -20)
    down()
    color('white')
    begin_fill()
    for _ in range(2):
        forward(240)
        left(90)
        forward(40)
        left(90)
    end_fill()
    up()
    goto(0, -12)
    color('black')
    write(text, align='center', font=('Arial', 20, 'bold'))
    update()


state = {'player': 0, 'game_over': False}
players = [drawx, drawo]
names = ['X', 'O']
board = [None] * 9


def tap(x, y):
    """Maneja el clic en el tablero."""
    if state['game_over']:
        return

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

    winner_player = winner()

    if winner_player is not None:
        show_message('¡Gana {}!'.format(names[winner_player]))
        state['game_over'] = True
    elif None not in board:
        show_message('¡Empate!')
        state['game_over'] = True
    else:
        update()
        state['player'] = 1 - player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
