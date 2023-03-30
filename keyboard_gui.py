import tkinter as tk
from tkinter import StringVar, ttk

from PIL import Image, ImageTk


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


def create_keyboard(frame, size: int):
    """
    Creates a keyboard used
    @param frame: the frame the keyboard is going into
    @size: the size of the button, the actual size of the keyboard is going to be width: size*3+24, height: size*4+32
    """
    keyboard = tk.Frame(frame)
    blank_image = tk.PhotoImage()  # This exists because if there is no image, the unit for the scaling defaults to
    # the text size
    for i in range(1, 11):
        if i == 10:
            button = tk.Button(keyboard, text=0, command=lambda: press_button(app, 0), height=size, width=size,
                               image=blank_image, compound="c")
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
            button.image = blank_image
        else:
            button = tk.Button(keyboard, text=i, command=lambda j=i: press_button(app, j), height=size, width=size,
                               image=blank_image, compound="c")
            button.grid(row=(i - 1) // 3, column=(i - 1) % 3)
            button.image = blank_image
    img = Image.open("Backspace.png")  # Note this image needs to be RGBA rather than LA (grayscale with transparency)
    # because imagetk will convert transparency to black if it is LA
    img = img.resize((size * 2 + 10, size + 2), Image.ANTIALIAS)
    backspace_image = ImageTk.PhotoImage(img)
    backspace_button = tk.Button(keyboard, text="test", image=backspace_image, command=lambda: backspace(app))
    backspace_button.image = backspace_image
    backspace_button.grid(row=3, column=1, columnspan=2)
    return keyboard


if __name__ == "__main__":
    """
    Sample running of a keyboard in a gui
    """
    app = tk.Tk()
    keyboard = create_keyboard(app, 50)

    app.title("Sample")
    val1 = StringVar()
    entry1 = ttk.Entry(app, textvariable=val1)
    val2 = StringVar()
    entry2 = ttk.Entry(app, textvariable=val2)

    entry1.grid(row=0, column=0)
    entry2.grid(row=1, column=0)
    keyboard.grid(row=2, column=0)

    app.mainloop()
