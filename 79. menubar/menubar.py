from tkinter import *

def openFile():
    print("File Opened")

def saveFile():
    print("File Saved")

def quit():
    print("Program Closed")

def cut():
    print("Cut")

def copy():
    print("Copy")

def paste():
    print("Paste")

window = Tk()

openImage = PhotoImage(file="open.png")
saveImage = PhotoImage(file="save.png")
quitImage = PhotoImage(file="quit.png")

menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Arial", 12))
menubar.add_cascade(label="File", menu=fileMenu)

fileMenu.add_command(label="Open", command=openFile, image=openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile, image=saveImage,compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit, image=quitImage, compound="left")

editMenu = Menu(menubar, tearoff=0,font=("Arial", 12))
menubar.add_cascade(label="Edit", menu=editMenu)

editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()