import tkinter as tk
from tkinter.simpledialog import askstring
import turtle
from tkinter import *

def initialise():
    global master, largeCogValue, smallCogValue, dValue

    master = Tk()
    master.minsize(1100,600)
    master.wm_title('Spyrograph')

    color_list = [
        "RED",
        "ORANGE",
        "YELLOW",
        "GREEN",
        "BLUE",
        "INDIGO",
        "VIOLET"]

    clicked = StringVar()
    clicked.set( "RED" )

    colorDropDown = OptionMenu(master, clicked, *color_list)
    colorDropDown.place(x=935,y=315)

    Label(master,text="Outer Cog:").place(x=955,y=370)
    largeCogValue = Scale(master,from_=5,to=100,orient=HORIZONTAL,command=cogSizeCheck)
    largeCogValue.place(x=935,y=395)

    Label(master,text="Inner Cog:").place(x=955,y=290)
    smallCogValue = Scale(master,from_=5,to=100,orient=HORIZONTAL,command=cogSizeCheck)
    smallCogValue.place(x=935,y=315)
    
    Label(master,text="D Value:").place(x=955,y=450)
    dValue = Scale(master, from_=2, to_=99, orient=HORIZONTAL,command=cogSizeCheck)
    dValue.place (x=935, y=475)

    confirmButton = Button(master,text="CONFIRM")
    confirmButton.place(x=950,y=525,w=75,h=40)

    canvas = tk.Canvas(master, background= "white", width=500, height= 500)

    canvas.place(x=270,y=50)

def cogSizeCheck(n):
    global largeCogValue, smallCogValue
    if largeCogValue.get() <= smallCogValue.get():
        print('large is smaller than small')
        print(largeCogValue.get())
        print(smallCogValue.get())
        largeCogValue.set(smallCogValue.get()+1)
        
    if dValue.get() == smallCogValue.get() + 10:
        dValue.set(smallCogValue.get() + 10)
        print("1")
        
    if dValue.get() < smallCogValue.get() - 10:
        dValue.set(smallCogValue.get() - 10)
        print("2")


initialise()
master.mainloop()
