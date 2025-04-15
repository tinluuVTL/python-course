from tkinter import *

def submit():
    username = entry.get()
    print(username)
    entry.config(state=DISABLED)
def delete():
    entry.delete(0, END)

def backspace():
    entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window, 
              font=("Arial", 20), 
              fg="green", 
              bg="lightblue", 
              show="*")
entry.insert(0, "Dimitar")
entry.pack(side=LEFT)

submit_button = Button(window, 
                       text="Submit", 
                       font=("Arial", 20),
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, 
                       text="Delete", 
                       font=("Arial", 20),
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, 
                          text="Backspace", 
                          font=("Arial", 20),
                          command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()