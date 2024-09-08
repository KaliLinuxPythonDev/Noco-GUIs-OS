from tkinter import *
from os import system

def clock():
	system("Applications/clock.py")

main = Tk()

clock_btn = Button(main,
	text="Clock")

clock_btn.pack()

main.mainloop()