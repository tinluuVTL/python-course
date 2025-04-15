from tkinter import *

def submit():
    print("The temperure is: " + str(scale.get()))

window =  Tk()

hotImage = PhotoImage(file="hot.gif")
hotLabel = Label(window, image=hotImage)
hotLabel.pack()

scale = Scale(window, 
    from_=1000, 
    to=0,
    length=600,
    orient=VERTICAL,
    font=("Comic Sans", 20),
    tickinterval=10,
    resolution=5,
    troughcolor="green",
    fg="blue",
    bg="lightblue",
    )
scale.set(((scale['from']-scale['to'])/2) + scale['to'])
scale.pack()

coldImage = PhotoImage(file="cold.gif")
coldLabel = Label(window, image=coldImage)
coldLabel.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()