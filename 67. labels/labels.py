from tkinter import *

window = Tk()

#  add photo
# photo = PhotoImage(file="icon.png")
# window.iconphoto(False, photo)

label = Label(window, 
                text="Hello World!", 
                font=("Arial", 40, "bold"), 
                fg="green", 
                bg="black",
                relief=SUNKEN,
                bd=10,
                padx=20,
                pady=20,
                # image=photo,
                # compound="bottom"
                )


# label["text"] = "Goodbye!"
# label["text"] = "Goodbye!"

label.pack()

# label.place(x=0, y=0)

window.mainloop()