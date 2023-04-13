from tkinter import *
from tkinter.ttk import *
import time

def start():
    tasks = 10
    x = 0
    while(x<tasks):
        time.sleep(1)
        bar['value']+=10
        x+=1
        window.update_idletasks

window = Tk()

bar = Progressbar (window,orient=HORIZONTAL, length=300)
bar.pack (pady=40)

button = Button(window,text="capture images", command=start).pack()
window.mainloop()