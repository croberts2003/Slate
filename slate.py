import sys

from tkinter import Text, Tk, Grid, Label, Pack, Button, IntVar, font, Menu, Menubutton

from tkinter import filedialog
from tkinter import messagebox

root = Tk("Slate")

root.title("Slate (Carson Schmidt)")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

def Font_Helvetica():
    global word_space
    word_space.config(font = "Helvetica")

def Font_Courier():
    global word_space
    word_space.config(font = "Courier")

def save_as():
    global word_space

    t = word_space.get("1.0", "end-1c")

    save_location = filedialog.asksaveasfilename()

    file1 = open(save_location, "w+")

    file1.write(t)

    file1.close()

#Buttons
word_space = Text(root)
word_space.grid(row = 1, columnspan = 2, padx = 10, pady = 10, )

inc = Label(root, text = "Welcome to Slate")
inc.grid(row = 0, column = 0)

save_button = Button(root, text = "Save", command = save_as)
save_button.grid(row = 0, column = 3)

font = Menubutton(root, text = "Font")
font.grid(row = 0, column = 2)

# learn the modern way to execute dropdown menus
font.menu = Menu(font, tearoff = 0)

font["menu"] = font.menu

Helvetica = IntVar()
arial = IntVar()
times = IntVar()
Courier = IntVar()
font.menu.add_checkbutton(label = "Courier", variable = Courier, command = Font_Courier)
font.menu.add_checkbutton(label = "Helvetica", variable = Helvetica, command = Font_Helvetica)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()