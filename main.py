from tkinter import *


# https://www.youtube.com/watch?v=yQSEXcf6s2I&list=PL_qj1UvvHaM2WD9ogveK0EEXZ86snJJX_&index=32&ab_channel=Codemy.com

root = Tk()
# creating a label widget
myLabel = Label(root, text="Hello World!")
myLabel1 = Label(root, text="Good grief Charlie Brown!")
# "Shoving" it onto the screen
# myLabel.pack()

myLabel.grid(row=0, column=0)
myLabel1.grid(row=1, column=1)

# mainloop() tells Python to run the Tkinter event loop.
# This method listens for events, such as button clicks or keypresses,
# and blocks any code that comes after it from running until you close the window where you called the method.

root.mainloop()


def print_hi(name):
    print(f'Hi, {name}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    print("Hello World.")
