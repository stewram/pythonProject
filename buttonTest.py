from tkinter import *

root = Tk()

e = Entry(root)
e.pack()
e.insert(0,"Enter your name: ")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


#padx and pady are optional and used to give more space around the button
myButton = Button(root, text="Enter your name.", padx=5, pady=5, command=myClick)
myButton.pack()


root.mainloop()