import tkinter as tk
from tkinter.simpledialog import askstring
import turtle


tina = turtle.Turtle()
tina.shape("turtle")

screen = turtle.Screen()
root = screen._root

controls = tk.Frame(root)
tk.Label(controls, text="Move forward:").pack(side=tk.LEFT)
fwd_entry = tk.Entry(controls)
fwd_entry.pack(side=tk.LEFT)
tk.Button(controls, text="Go!", command=lambda: tina.forward(int(fwd_entry.get()))).pack(side=tk.LEFT)
controls.pack()

tina_color = askstring("Tina's color", "What color should Tina the turtle be?")
bg_color = askstring("The background color", "What color should the background be?")
tina.color(tina_color)
screen.bgcolor(bg_color)

root.mainloop()