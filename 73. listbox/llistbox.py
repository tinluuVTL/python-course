from tkinter import *

def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))

    print("You have selected " + ", ".join(food))
    # print(listbox.get(listbox.curselection()))


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())

def delete():
    # listbox.delete(listbox.curselection())
    # listbox.config(height=listbox.size())

    for index in reversed(listbox.curselection()):
        listbox.delete(index)
    listbox.config(height=listbox.size())


window = Tk()

listbox = Listbox(window,
                  bg="lightgreen",
                  font=("Consolas", 20),
                  height=4,
                  width=15,
                  selectbackground="gray",
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1, 'pizza')
listbox.insert(2, 'pasta')
listbox.insert(3, 'garlic bread')
listbox.insert(4, 'soup')
listbox.insert(5, 'salad')

listbox.config(height=listbox.size())

entry_box = Entry(window, font=("Consolas", 20))
entry_box.pack()

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack()

add_button = Button(window, text="Add", command=add)
add_button.pack()

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack()

window.mainloop()