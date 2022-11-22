#!/usr/bin/env python3

import turtle
import random 
from PIL import Image

SIZE = 1000
DENSITY = 40

t = turtle.Turtle()
s = turtle.Screen()

s.setup(SIZE, SIZE)
s.colormode(255)
t.pensize(3)
t.speed(0)

t.penup()

def draw_line(row, col):
    lower_left = (
        (col * SIZE / DENSITY) - SIZE / 2,
        (row * SIZE / DENSITY) - SIZE / 2
    )
    upper_right = (
        ((col + 1) * SIZE / DENSITY) - SIZE / 2,
        ((row + 1) * SIZE / DENSITY) - SIZE / 2
    )
    lower_right = (
        ((col + 1) * SIZE / DENSITY) - SIZE / 2,
        (row * SIZE / DENSITY) - SIZE / 2
    )
    upper_left = (
        (col * SIZE / DENSITY) - SIZE / 2,
        ((row + 1) * SIZE / DENSITY) - SIZE / 2
    )

    res = random.randint(0, 1)
    r = random.randint(1,255)
    t.pencolor(r,150,90)

    if res == 0:
        t.goto(upper_left)
        t.pendown()
        t.goto(lower_right)
        t.penup()
    else:
        t.goto(lower_left)
        t.pendown()
        t.goto(upper_right)
        t.penup()

for row in range(DENSITY):
    for col in range(DENSITY):
        draw_line(row, col)

canvas = s.getcanvas()
canvas.postscript(file='example.eps', width=SIZE, height=SIZE)
img = Image.open('example.eps') 
img.save('example.jpg')  
s.exitonclick()
