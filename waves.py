# Adding waves

import math, turtle
from turtle import *
bgcolor("black")

a1 = numinput("A1", "Amplitude Wave 1: ", 0, minval=-3, maxval=3)
f1 = numinput("F1", "Frequency Wave 1: ", 0, minval=-10, maxval=10)
p1 = numinput("P1", "Phi Wave 1: ", 0, minval=-6.283185, maxval=6.283185)
a2 = numinput("A2", "Amplitude Wave 2: ", 0, minval=-3, maxval=3)
f2 = numinput("F2", "Frequency Wave 2: ", 0, minval=-10, maxval=10)
p2 = numinput("P2", "Phi Wave 2: ", 0, minval=-6.283185, maxval=6.283185)

# draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# write label at location x, y
def labelPoint (ttl, x, y, label):
  ttl.penup()
  ttl.goto (x, y)
  ttl.pendown()
  ttl.write (label)
  ttl.penup()

def drawGridMark (ttl, x, y, isVertical):
  if isVertical :
    drawLine (ttl, x, y + 5, x, y - 5)
  else:
    drawLine (ttl, x - 5, y, x + 5, y)

def labelGridPoint (ttl, x, y, isVertical, text):
  if isVertical:
    labelPoint (ttl, x - 20, y - 20, text)
  else:
    labelPoint (ttl, x + 20, y, text)

def drawGridScaled (ttl):
  # draw the axes
  drawLine (ttl, -400, 0, 400, 0)
  drawLine (ttl, -400, 400, -400, -400)

  # label the x axis
  for x in [-400, -300, -200, -100, 0, 100, 200, 300]:
    drawGridMark (ttl, x, 0, True)
    labelGridPoint (ttl, x, 0, True, (x/100 + 4, 0))

  # label the y axis
  for y in [-300, -200, -100, 100, 200, 300]:
    drawGridMark (ttl, -400, y, False)
    labelGridPoint (ttl, -400, y, False, (0, y/100))

def drawFnScaled (ttl, fn, lower, upper, step):
  ttl.penup()
  x = lower
  y = fn (x)
  scaledX = x * 100 -400
  scaledY = y * 100
  ttl.goto (scaledX, scaledY)
  ttl.pendown()
  while x < upper:
    x = x + step
    y = fn ( x )
    scaledX, scaledY = x * 100 - 400, y * 100
    ttl.goto (scaledX, scaledY)
  ttl.penup()

def wave1 (x):
  return (a1 * math.cos((2.0 * math.pi * f1 * x) + p1))

def wave2 (x):
  return (a2 * math.cos((2.0 * math.pi * f2 * x) + p2))

def waveSum (x):
  return (wave1(x) + wave2(x))

def  main():
  # put label on top of page
  turtle.title ('Graphs of Waves')

  # setup screen size
  turtle.setup (800, 800, 0, 0)

  # create a turtle object
  ttl = turtle.Turtle()
  ttl.speed(0)

  # draw the grid
  ttl.color("white")
  drawGridScaled (ttl)

  # draw wave 1
  ttl.pencolor ('red')
  drawFnScaled (ttl, wave1, 0, 7, 0.01)

  # draw wave 2
  ttl.pencolor ('blue')
  drawFnScaled (ttl, wave2, 0, 7, 0.01)

  # draw sum
  ttl.pencolor ('green')
  drawFnScaled (ttl, waveSum, 0, 7, 0.01)

  # persist drawing
  turtle.done()


main()
