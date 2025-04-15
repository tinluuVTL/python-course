from tkinter import *

def submit():
    input = text.get("1.0", END)
    print(input)

window = Tk()

text = Text(window, 
            bg="lightblue", 
            fg="black",
            font=("Consolas", 20), 
            height=5, 
            width=30,
            padx=10,
            pady=10
            )
text.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()