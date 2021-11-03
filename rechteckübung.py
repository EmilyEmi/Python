import turtle
import random
from random import randint

mytutu = turtle.Turtle()


def rechteck(laenge, hoehe):
    mytutu.forward(laenge)
    mytutu.right(90)
    mytutu.forward(hoehe)
    mytutu.right(90)
    mytutu.forward(laenge)
    mytutu.right(90)
    mytutu.forward(hoehe)


def positionieren(abstand):
    mytutu.penup()
    mytutu.right(90)
    mytutu.forward(abstand)
    mytutu.right(90)
    mytutu.forward(abstand)
    mytutu.left(90)
    mytutu.pendown()



def rechteck_schoner(abstand, laenge, hoehe,startX,startY):
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