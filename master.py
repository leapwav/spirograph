import tkinter as tk
from tkinter.simpledialog import askstring
import turtle
from tkinter import *
import math

def initialise():
    global master, largeCogValue, smallCogValue, dValue, myturtle, colorDropDown, clicked, canvas, clear

    master = Tk()
    master.minsize(1100,600)
    master.wm_title('Spyrograph')
    
    canvas = tk.Canvas(master, background= "white", width=500, height= 500)

    canvas.place(x=270,y=50)


    myturtle = turtle.RawTurtle(canvas)
    myturtle.hideturtle()
    myturtle.speed("fastest")

    myturtle.up()

    color_list = [
        "BLACK",
        "RED",
        "ORANGE",
        "YELLOW",
        "GREEN",
        "BLUE",
        "MAGENTA"]

    clicked = StringVar()
    clicked.set( "BLACK" )

    Label(master,text="Colour:").place(x=955,y=225)

    colorDropDown = OptionMenu(master, clicked, *color_list,command=colorSys)
    colorDropDown.place(x=940,y=250)

    Label(master,text="Outer Cog:").place(x=955,y=370)
    largeCogValue = Scale(master,from_=5,to=100,orient=HORIZONTAL,command=cogSizeCheck)
    largeCogValue.place(x=935,y=395)

    Label(master,text="Inner Cog:").place(x=955,y=290)
    smallCogValue = Scale(master,from_=5,to=99,orient=HORIZONTAL,command=cogSizeCheck)
    smallCogValue.place(x=935,y=315)
    
    Label(master,text="D Value:").place(x=955,y=450)
    dValue = Scale(master, from_=2, to_=99, orient=HORIZONTAL,command=cogSizeCheck)
    dValue.place (x=935, y=475)

    confirmButton = Button(master,text="CONFIRM",command=confirm)
    confirmButton.place(x=950,y=525,w=75,h=40)
    
    boredButton = Button(master,text="bored",command=winston)
    boredButton.place(x=950,y=10,w=75,h=40)

    clearButton = Button(master, text="CLEAR", command=lambda:clear_function())
    clearButton.place(x=135, y=475,w=75,h=40)
    
    
def cogSizeCheck(n):
    global largeCogValue, smallCogValue
    if largeCogValue.get() <= smallCogValue.get():
        print('large is smaller than small')

        largeCogValue.set(smallCogValue.get()+1)
        
    if dValue.get() == smallCogValue.get() + 10:
        dValue.set(smallCogValue.get() + 10)
        print("1")
        
    if dValue.get() < smallCogValue.get() - 10:
        dValue.set(smallCogValue.get() - 10)
        print("2")

def confirm():
    global largeCogValue, smallCogValue, dValue, myturtle, clear
    
    clear = False
    largeCogValue=largeCogValue.get()
    smallCogValue=smallCogValue.get()
    dValue=dValue.get()
    
    constant = 240/(largeCogValue-smallCogValue+dValue)
    print(largeCogValue,smallCogValue,dValue)
    
    for t in range(0,3600000000000000,10):
        radt = t*0.017
        if t != 0 and clear == False:
            myturtle.down()
        elif clear == True:
            break
        myturtle.setposition(int(constant*((largeCogValue-smallCogValue)*math.cos(radt))-constant*dValue*math.cos(largeCogValue/smallCogValue*radt-radt)), int(constant*((largeCogValue-smallCogValue)*math.sin(radt))-constant*dValue*math.sin(largeCogValue/smallCogValue*radt-radt)))
        myturtle.up()
            
    
def winston():
    print('winston')
    import video
    
def colorSys(self):
    global colorDropDown,clicked,myturtle
    myturtle.color(clicked.get().lower())
    
def clear_function():
    global canvas, clear
    myturtle.up()
    canvas.delete("all")
    master.destroy()
    clear = True
    initialise()
        
initialise()
master.mainloop()
