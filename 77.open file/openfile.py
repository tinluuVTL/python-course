from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir = "/", 
                                          title = "Open file", 
                                          filetypes = (("Text files", "*.txt"), ("all files", "*.*")))

    file = open(filepath, 'r')
    print(file.read())
    file.close()

window = Tk()

button = Button(window, text="Open File", command=openFile)
button.pack()

window.mainloop()