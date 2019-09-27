import turtle
import math

class arm:
    def __init__(self,length,angVelo):
        self.l=length
        self.aV=angVelo
        self.angle=0

    def update(self):
        self.angle = self.angle + self.aV

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


pen = turtle.Turtle() 
pen.hideturtle()
pen.penup()
pen.pensize(2)

window = turtle.Screen()
window.bgcolor('#ffffff')

while(True):
    spi.penup()
    spi.setpos(0,0)
    spi.pendown()
    for x in range(len(armList)):
        if(x==0):
            spi.setheading(armList[x].angle)
        else:
            spi.setheading(armList[x].angle + armList[x-1].angle)
        spi.forward(armList[x].l)
        armList[x].update()
    
    pen.setpos(spi.pos())
    pen.penup()
    pen.pendown()
    spi.clear()
