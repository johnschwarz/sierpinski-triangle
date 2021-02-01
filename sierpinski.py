import turtle as t
import random
import numpy
a = numpy.array([-200,200])
b = numpy.array([0,0])
c = numpy.array([200,200])
current = numpy.array([random.randint(-100,100), random.randint(-100,100)])

t.speed(0)
t.pu()
t.setpos(current)
for i in range(4000):
  x = random.randint(1,3)
  if x == 1:
    current = (current - a)/2
  elif x == 2:
    current = (current - b)/2
  elif x == 3:
    current = (current - c)/2
  t.setpos(current)
  t.dot(4, "black")
