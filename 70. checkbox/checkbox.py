from tkinter import *

def display():
    if(x.get() == 1):
        print('You agree!')
    else:
        print('You do not agree!')

window = Tk()

x = BooleanVar()

python_photo = PhotoImage(file="python.png")

check_button = Checkbutton(window, 
                           text="I agree with everything", 
                           variable=x,
                           onvalue=True, 
                           offvalue=False,
                           command=display, 
                           font=("Arial", 20), 
                           fg="green", 
                           bg="lightblue", 
                           activeforeground="green", activebackground="lightblue",
                            padx=20, pady=20,
                            image=python_photo,
                            compound="bottom")
check_button.pack()

window.mainloop()