# File: SeychellesFlag.py
# Student: Arshia Riaz
#
# Date Created: 11/26/2021
# Date Last Modified: 11/29/2021
# Description of Program: This program produces the flag of the Seychelles. 

import turtle

def rectangle(a,x,y,l,h):
        a.up()
        a.goto(x,y)
        a.setheading(0)
        a.down()
        for i in range(2) :
                a.forward(l)
                a.right(90)
                a.forward(h)
                a.right(90)
        a.up()

def triangle(a,x1,y1,x2,y2,x3,y3):
        a.up()
        a.goto(x1,y1)
        a.down()
        a.goto(x2,y2)
        a.goto(x3,y3)
        a.goto(x1,y1)
        a.up()

def quadrilateral(a,x1,y1,x2,y2,x3,y3,x4,y4):
        a.up()
        a.goto(x1,y1)
        a.down()
        a.goto(x2,y2)
        a.goto(x3,y3)
        a.goto(x4,y4)
        a.goto(x1,y1)
        a.up()

def fillTriangle(a,x1,y1,x2,y2,x3,y3,color) :
        a.fillcolor(color)
        a.begin_fill()
        triangle(a,x1,y1,x2,y2,x3,y3)
        a.end_fill()

def fillquadrilateral(a,x1,y1,x2,y2,x3,y3,x4,y4,color) :
        a.fillcolor(color)
        a.begin_fill()
        quadrilateral(a,x1,y1,x2,y2,x3,y3,x4,y4)
        a.end_fill()

turtle.setup(1500,1000,0, 0)

myBlue = '#003D88'
myYellow = '#FCD955'
myRed = '#D72323'
myWhite = '#FFFFFF'
myGreen = '#007B3A'

b = turtle.Turtle()
rectangle(b,0, 300,600,300)
b.goto(0,0)

fillTriangle(b,0, 0, 0,300,200,300,myBlue)

fillTriangle(b,0, 0, 200,300,400,300,myYellow)

fillquadrilateral(b,0, 0, 400,300,600,300,600,200,myRed)

fillTriangle(b,0, 0, 600,200,600,100,myWhite)

fillTriangle(b,0, 0, 600,100,600,0, myGreen)

ts = turtle.getscreen()
tc = ts.getcanvas()
turtle.done()
