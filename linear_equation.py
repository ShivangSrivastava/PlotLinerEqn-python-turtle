from turtle import *
from math import atan, pi


class Plotting:
    def __init__(self, eqn):
        self.eqn = eqn
        self.a = 1
        self.b = 1
        self.c = 1
        self.m = 0

    def abc_sep(self):
        try:
            a = float(self.eqn.split("x")[0])
        except ValueError:
            a = float(self.eqn.split("x")[0] + "1")
        try:
            b = float(self.eqn.split("x")[1].split("y")[0])
        except ValueError:
            b = float(self.eqn.split("x")[1].split("y")[0] + "1")
        c1 = self.eqn.split("x")[1].split("y")[1].split("=")
        try:
            con1 = float(c1[0])
        except ValueError:
            con1 = 0
        try:
            con2 = float(c1[1])
        except ValueError:
            con2 = 0
        c = con1 - con2
        self.a = a
        self.b = b
        self.c = c

    def slope(self):
        try:
            r = atan(-self.a/self.b)
            self.m = 180*r/pi
        except ZeroDivisionError:
            self.m = 90

    def plot(self, clr="blue"):
        self.abc_sep()
        self.slope()
        try:

            c = -self.c/self.b
            penup()
            pencolor(clr)
            goto(0, c)
            seth(self.m)
            pendown()
            fd(500)
            bk(1000)
        except ZeroDivisionError:
            penup()
            pencolor(clr)
            goto(-self.c/self.a, 0)
            seth(self.m)
            pendown()
            fd(500)
            bk(1000)


pencolor("red")
ht()
speed(0)
for i in range(4):
    seth(i*90)
    fd(500)
    goto(0, 0)

t1 = Pen()
t2 = Pen()
t3 = Pen()
t4 = Pen()
t1.speed(0)
t2.speed(0)
t3.speed(0)
t4.speed(0)
t1.seth(90)
t2.seth(0)
t3.seth(270)
t4.seth(180)
t1.ht()
t2.ht()
t3.ht()
t4.ht()
i = 0
while i < 500:
    t1.penup()
    t2.penup()
    t3.penup()
    t4.penup()
    t1.goto(i, 0)
    t2.goto(0, i)
    t3.goto(-i, 0)
    t4.goto(0, -i)
    t1.pendown()
    t2.pendown()
    t3.pendown()
    t4.pendown()
    t1.fd(5)
    t2.fd(5)
    t3.fd(5)
    t4.fd(5)
    i += 20

n = int(input("Number of eqn:  "))
for _ in range(n):
    eq = input(
        "\neqn must be in form of ax+by+c=0\n"
        "e.g. 2x+3y=5\n"
        " >>> "
             )
    col = input("Color of line:\n >>")
    pl = Plotting(eq)
    pl.plot(col)


done()
