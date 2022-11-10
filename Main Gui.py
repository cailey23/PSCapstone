from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime
import random
import time
from turtle import TurtleScreen, bgcolor



window = Tk()
window.title("TimeLapseProgram")


notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab2 = Frame(notebook)
tab3 = Frame(notebook)

notebook.add(tab1,text="Calculator")
notebook.add(tab2,text="CameraControler")
notebook.add(tab3,text="VideoProducer")
notebook.pack(expand=True,fill="both")

Label1 = Label(tab1,bd=10,bg="orange",width=200,height=100,relief=RIDGE).grid()
Top_Label1_Frame = Label(Label1, bd=10,bg="orange",width=200,height=50,relief=RIDGE).pack()
Label2 = Label(tab2,bd=10,bg="orange",width=200,height=100,relief=RIDGE).grid()

Label3 = Label(tab3,bd=10,bg="orange",width=200,height=100,relief=RIDGE).grid()

clip_length = StringVar()
event_duration = StringVar()
frame_rate = StringVar()



window.mainloop()
