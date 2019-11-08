import turtle
import math
class arm:
    def __init__(self,r,angVelo):
        self.rad = r
        self.aV = angVelo
        self.angle = 0

    def update(self):
        self.angle = self.angle + self.aV


arms = 2
arm1Len = float(input("Enter length of arm 0: "))
arm1AV= float(input("Enter angular velocity of arm 0: "))
armList = [arm(arm1Len,arm1AV)]

for x in range(1,int(arms)):
    leng=float(input("Enter length of arm " + str(x) + ": "))
    av=float(input("Enter angular velocity of arm " + str(x)+ ": "))
    armList.append(arm(leng,av))

window = turtle.Screen()
window.bgcolor('#ffffff')

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

while(True):
    spi.penup()
    spi.setpos(0,0)
    
    spi.setheading(armList[0].angle)
    spi.forward(armList[0].rad)
    spi.setheading(armList[0].angle + armList[1].angle)
    spi.pendown()
    spi.forward(armList[1].rad)
    armList[0].update()
    armList[1].update()
