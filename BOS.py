from tkinter import *
from os import system

def boot():
	os.system("main.py")
	exit()

bos = Tk()
bos.title("BOS")
bos.attributes("-fullscreen", True)

boot_btn = Button(bos,
				text="Boot Into OS",
				command=boot)

boot_btn.pack(anchor=CENTER)

bos.mainloop()
