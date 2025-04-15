from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print('You ordered pizza')
    elif(x.get() == 1):
        print('You ordered hamburger')
    else:
        print('You ordered hotdog')

window = Tk()

x = IntVar()

pizzaImage = PhotoImage(file="pizza.png")
hamburgerImage = PhotoImage(file="hamburger.png")
hotdogImage = PhotoImage(file="hotdog.png")

foodImages = [pizzaImage,hamburgerImage,hotdogImage]

for index in range(len(food)):
    radiobutton = Radiobutton(window, 
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=("Arial", 15),
                              image=foodImages[index],
                              compound="left",
                              indicatoron=0,
                              width=375,
                              command=order
                              )
    radiobutton.pack(anchor=W)

window.mainloop()