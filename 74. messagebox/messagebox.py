from tkinter import *
from tkinter import messagebox

def click():
    # messagebox.showinfo(title="Message", message="Hello World")
    # messagebox.showinfo("Message", "Hello World")
    # messagebox.showwarning("Warning", "Hello World")
    # messagebox.showerror("Error", "Hello World")
    # messagebox.askquestion("Question", "Hello World")
    # messagebox.askokcancel("OK Cancel", "Hello World")
    # messagebox.askyesno("Yes No", "Hello World")
    # messagebox.askretrycancel("Retry Cancel", "Hello World")

    if messagebox.askokcancel("OK Cancel", "Hello World"):
        print("Yes")
    else:
        print("No")

window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()