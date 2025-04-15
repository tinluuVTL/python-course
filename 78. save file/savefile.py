from tkinter import *
from tkinter import filedialog

def save():
    file = filedialog.asksaveasfile(initialdir="/Users/dimitarmitev/Desktop/python-course/78. save file", 
                                defaultextension=".txt", 
                                filetypes=[
                                    ("All Files", "*.*"), 
                                    ("Text Documents", "*.txt"), 
                                    ("HTML files", "*.html")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    # filetext = input("Enter some text: ")
    file.write(filetext)
    file.close()

window = Tk()

button = Button(window, text="Save", command=save)
button.pack()
text = Text(window)
text.pack()

window.mainloop()