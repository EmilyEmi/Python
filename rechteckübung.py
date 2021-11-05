import turtle
import random
from random import randint

mytutu = turtle.Turtle()

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
#rechteck(-150,100,250,200)


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
            rechteck(start1x,start1y,laenge1,hoehe1)
            rechteck_schoner(abstand,laenge1,hoehe1,start1x,start1y)
            rechteck(start2x,start2y,laenge2,hoehe2)
            rechteck_schoner(abstand,laenge2,hoehe2,start2x,start2y)
        elif laenge>2*abstand:
            laenge1 = laenge-2*abstand
            hoehe1 = randint(1,hoehe-3*abstand)
            start2x = start1x
            start2y = start1y-hoehe1-abstand
            hoehe2 = hoehe-hoehe1-3*abstand
            laenge2 = laenge1
            rechteck(start1x, start1y, laenge1, hoehe1)
            rechteck_schoner(abstand, laenge1, hoehe1, start1x, start1y)
            rechteck(start2x, start2y, laenge2, hoehe2)
            rechteck_schoner(abstand, laenge2, hoehe2, start2x, start2y)
rechteck_schoner(5,300,50,-100,100)
"""""

    if laenge>3*abstand and hoehe>2*abstand:
        if 9*abstand<laenge:
             rechteck(laenge, hoehe)
            positionieren(abstand)
            mytutuPosition = mytutu.pos()
            x=mytutuPosition[0]
            y=mytutuPosition[1]
            print(x)
            print(y)


            laenge1 = randint(3*abstand,laenge-6*abstand)
            if laenge1>3*abstand:
                rechteck(laenge1,hoehe-2*abstand)

                mytutu.right(90)
                mytutu.penup()
                mytutu.forward(laenge1+abstand)
                mytutu.pendown()

                laenge2 = laenge-laenge1-3*abstand
                if laenge2>3*abstand:
                    rechteck(laenge2,hoehe-2*abstand)
                    mytutu.penup()
                    mytutu.goto(mytutuPosition)
                    mytutu.pendown()
                    mytutu.right(90)

    rechteck_schoner(abstand,laenge1,hoehe-2*abstand,x,y)
    rechteck_schoner(abstand,laenge2, hoehe - 2 * abstand, x+laenge1+abstand, y)






rechteck_schoner(10,300,300,0,0)
"""""