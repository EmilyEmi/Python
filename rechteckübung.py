import turtle
import random
from random import randint

mytutu = turtle.Turtle()
mytutu.speed(3)
screen = turtle.getscreen()
screen.clear()
screen.title("Game")
screen.colormode(255)

def colors():
    colors = []
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    colors.append(r)
    colors.append(g)
    colors.append(b)
    return colors


#schritt1

def rechteck(startx,starty,laenge, hoehe):
    mytutu.penup()
    mytutu.goto(startx,starty)
    mytutu.pendown()
    mytutu.forward(laenge)
    mytutu.right(90)
    mytutu.forward(hoehe)
    mytutu.right(90)
    mytutu.forward(laenge)
    mytutu.right(90)
    mytutu.forward(hoehe)
    mytutu.right(90)



#Schritt2
def candraw2boxes(laenge,hoehe,abstand):
    if laenge>3*abstand and hoehe>2*abstand:
        return True
    elif laenge>2*abstand and hoehe>3*abstand:
        return True
    else:
        return False



def positionieren(abstand):
    mytutu.penup()
    mytutu.right(90)
    mytutu.forward(abstand)
    mytutu.right(90)
    mytutu.forward(abstand)
    mytutu.left(90)
    mytutu.pendown()



def rechteck_schoner(abstand, laenge, hoehe,startX,startY):
    rechteck(startX,startY,laenge,hoehe)
    draw2boxes=candraw2boxes(laenge,hoehe,abstand)
    if draw2boxes:
        start1x=startX+abstand
        start1y= startY-abstand
        if laenge>3*abstand:
            laenge1 = randint(1,laenge-3*abstand)
            hoehe1 = hoehe-2*abstand
            start2x = start1x + laenge1+abstand
            start2y = start1y
            laenge2 = laenge-laenge1-3*abstand
            hoehe2 = hoehe1
        elif laenge>2*abstand:
            laenge1 = laenge-2*abstand
            hoehe1 = randint(1,hoehe-3*abstand)
            start2x = start1x
            start2y = start1y-hoehe1-abstand
            hoehe2 = hoehe-hoehe1-3*abstand
            laenge2 = laenge1
        rechteck_schoner(abstand, laenge1, hoehe1, start1x, start1y)
        rechteck_schoner(abstand, laenge2, hoehe2, start2x, start2y)
rechteck_schoner(20,400,200,-100,100)