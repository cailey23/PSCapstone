import tkinter as tk
from tkinter import BOTTOM, TOP, StringVar, ttk
from typing import List


def press_button(app, val):
    """
    gets the entry selected and puts a value on the end
    """
    widget = app.focus_get()
    widget.insert("end", val)


def backspace(app):
    """
    gets the entry selected and removes a value on the end
    """
    widget = app.focus_get()
    widget.delete(len(widget.get()) - 1, "end")


def create_keyboard(frame):
    """
    Creates a keyboard used
    """
    keyboard = tk.Frame(frame)
    for i in range(1, 11):
        if i == 10:
            button = tk.Button(keyboard, text=0, command=lambda: press_button(app, 0))
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
        else:
            button = tk.Button(keyboard, text=i, command=lambda j=i: press_button(app, j))
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
    backspace_image = tk.PhotoImage(file="Backspace.png")
    backspace_button = tk.Button(keyboard, text="test", image=backspace_image, command=lambda: backspace(app))
    backspace_button.image = backspace_image
    backspace_button.grid(row=3, column=1, columnspan=2)
    return keyboard


if __name__ == "__main__":
    """
    Sample running of a keyboard in a gui
    """
    app = tk.Tk()
    keyboard = create_keyboard(app)
    app.title("Sample")
    val1 = StringVar()
    entry1 = ttk.Entry(app, textvariable=val1)
    val2 = StringVar()
    entry2 = ttk.Entry(app, textvariable=val2)

    entry1.grid(row=0, column=0)
    entry2.grid(row=1, column=0)
    keyboard.grid(row=2, column=0)

    app.mainloop()
