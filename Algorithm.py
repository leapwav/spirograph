import turtle
import math

myturtle = turtle.Turtle()
myturtle.hideturtle()
myturtle.speed("fastest")
largeCogValue = 80
smallCogValue = 57
dValue = 7
myturtle.up()

for t in range(0,3600000000000000,10):

    radt = t*0.017
    if t != 0:
        myturtle.down()
    
    myturtle.setposition(int((100/largeCogValue)*((largeCogValue-smallCogValue)*math.cos(radt))-(500/largeCogValue)*dValue*math.cos(largeCogValue/smallCogValue*radt-radt)), int((500/largeCogValue)*((largeCogValue-smallCogValue)*math.sin(radt))-(500/largeCogValue)*dValue*math.sin(largeCogValue/smallCogValue*radt-radt)))
    myturtle.up()
