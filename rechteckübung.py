import turtle

mytutu = turtle.Turtle()

mytutu.speed(100)
mytutu.penup()
mytutu.left(135)
mytutu.forward(450)
mytutu.pendown()
mytutu.right(135)

def rechteck(laenge,breite):

    mytutu.forward(breite)
    mytutu.right(90)
    mytutu.forward(laenge)
    mytutu.right(90)
    mytutu.forward(breite)
    mytutu.right(90)
    mytutu.forward(laenge)
rechteck(600,500)

def rechteck2(abstand,laenge,breite):
    if laenge > abstand:
        mytutu.penup()
        mytutu.right(90)
        mytutu.forward(abstand)
        mytutu.right(90)
        mytutu.forward(abstand)
        mytutu.left(90)
        mytutu.pendown()
        rechteck(laenge-2*abstand,breite-2*abstand)
        rechteck2(abstand,laenge-2*abstand,breite-2*abstand)




rechteck2(20,400,500)
