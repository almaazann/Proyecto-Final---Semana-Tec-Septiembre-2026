"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path


# Imagen utilizada para representar las fichas del juego
car = path('car.gif')

# Se crean pares de números para formar las tarjetas de memoria
tiles = list(range(32)) * 2

# Guarda la ficha seleccionada y el numero de movimientos realizados
state = {'mark': None, 'pairs': 0}

# Indica qué fichas permanecen ocultas
hide = [True] * 64


def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


# Esta función controla lo que ocurre cuando el jugador selecciona una ficha
def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)

    # Evita errores si se hace clic fuera del tablero
    if spot < 0 or spot >= len(tiles):
        return

    mark = state['mark']

    # Guarda la primera ficha seleccionada o cambia la selección
    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        # Si las dos fichas coinciden, permanecen descubiertas
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None

        # Cuenta y muestra los pares descubiertos
        state['pairs'] += 1
        print('Pares descubiertos:', state['pairs'])

        # Comprueba si todas las fichas fueron descubiertas
        if not any(hide):
            print('Juego completado')


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()

