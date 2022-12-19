import pgzrun
import random

WIDTH = 800
HEIGHT = 600

sun = Actor("sun")
sun.timer = 0
sun.points = 0


def draw():
    screen.fill("skyblue")
    sun.draw()
    screen.draw.text(str(sun.points), center=(WIDTH / 2, 50), color="red", fontsize=100)


def update():
    sun.timer -= 1

    if sun.timer <= 0:
        sun.x = random.randint(80, WIDTH - 80)
        sun.y = random.randint(80, HEIGHT - 80)
        sun.timer = 60 - sun.points


def on_mouse_down(pos):
    if sun.collidepoint(pos):
        sun.points += 1
        sun.timer = 0
    else:
        sun.points -= 1
        sun.timer = 0


pgzrun.go()
