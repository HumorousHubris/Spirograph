import turtle
import math

class arm:
    def __init__(self,length,angVelo):
        self.l=length
        self.aV=angVelo
        self.angle=0

    def update(self):
        self.angle = self.angle + self.aV

lineMode = False

arms = int(input("Input number of arms: "))
arm1Len = float(input("Enter length of arm 0: "))
arm1AV= float(input("Enter angular velocity of arm 0: "))
armList = [arm(arm1Len,arm1AV)]

for x in range(1,int(arms)):
    leng=float(input("Enter length of arm " + str(x) + ": "))
    av=float(input("Enter angular velocity of arm " + str(x)+ ": "))
    armList.append(arm(leng,av))

spi = turtle.Turtle()
spi.pensize(1)
spi.speed(0)
spi.color('#4bec13')
spi.hideturtle()
spi.speed('fastest')
turtle.tracer(5,0)

pen = turtle.Turtle() 
pen.hideturtle()
pen.penup()
pen.pensize(2)
pen.speed('fastest')

window = turtle.Screen()
window.bgcolor('#ffffff')

rootwindow = window.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')


while(True):
    spi.penup()
    spi.setpos(0,0)
    if(not lineMode):
        spi.pendown()

    
    for x in range(len(armList)):
        if(x==0):
            spi.setheading(armList[x].angle)
        else:
            spi.setheading(armList[x].angle + armList[x-1].angle)
        if(x==len(armList)-1 and lineMode):
            spi.pendown()
        spi.forward(armList[x].l)
        armList[x].update()
    
    pen.setpos(spi.pos())
    pen.penup()
    pen.pendown()
    if(not lineMode):
        spi.clear()

##    if(armList[0].angle > 400):
##        break
