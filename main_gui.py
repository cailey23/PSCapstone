from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import datetime
import random
import time
from turtle import TurtleScreen, bgcolor
import PySimpleGUI as sg



window = Tk()
window.title("TimeLapseProgram")


notebook = ttk.Notebook(window)
tab1 = Frame(notebook)
tab1.pack()
tab2 = Frame(notebook)
tab2.pack()
tab3 = Frame(notebook)
tab3.pack()

notebook.add(tab1,text="Calculator")
notebook.add(tab2,text="CameraControler")
notebook.add(tab3,text="VideoProducer")
notebook.pack(expand=True,fill="both")

#Calculator
Tab1_Label1 = Label(tab1, text="Calculate:")
Tab1_Label1.grid(row=0)
course = ["Event duration","Clip length","Shooting interval"]
Tab1_cmb1 = ttk.Combobox(tab1,value=course, width=18)
Tab1_cmb1.grid(row=0, column=1)

Tab1_Label2 = Label(tab1, text="Shooting interval:")
Tab1_Label2.grid(row=1)
Tab1_Entry1 = Entry(tab1)
Tab1_Entry1.grid(row=1, column=1)

Tab1_Label3 = Label(tab1, text="Clip length:")
Tab1_Label3.grid(row=2)
Tab1_Entry2 = Entry(tab1)
Tab1_Entry2.grid(row=2, column=1)

Tab1_Label4 = Label(tab1, text="Frames per second:")
Tab1_Label4.grid(row=3)
course2 = ["6","12","15","24","30"]
Tab1_cmb2 = ttk.Combobox (tab1, value=course2, width=18)
Tab1_cmb2.grid(row=3, column=1)

Tab1_Label5 = Label(tab1, text="Event duration:")
Tab1_Label5.grid(row=4)
Tab1_Entry3 = Entry(tab1)
Tab1_Entry3.grid(row=4, column=1)

#CameraControl
#PYSimpleGUIqt to make the preview window but need pyside2 which needs python 3.10 or lower vision
Tab2_Label1 = Label(tab2, text="Shutter Speed:")
Tab2_Label1.grid(row=0)
course = ["1/2","1/4","1/8","1/15","1/30","1/60","1/125","1/250","1/500","1/1000"]
Tab2_cmb1 = ttk.Combobox(tab2,value=course, width=18)
Tab2_cmb1.grid(row=0, column=1)

Tab2_Label2 = Label(tab2, text="Aperture:")
Tab2_Label2.grid(row=1)
course2 = ["1.4","2","2.8","4","5.6","8","11","16","22"]
Tab2_cmb2 = ttk.Combobox(tab2,value=course2, width=18)
Tab2_cmb2.grid(row=1, column=1)

Tab2_Label3 = Label(tab2, text="ISO:")
Tab2_Label3.grid(row=2)
course3 = ["50","100","200","400","800","1600","3200","6400"]
Tab2_cmb3 = ttk.Combobox(tab2,value=course3, width=18)
Tab2_cmb3.grid(row=2, column=1)

Tab2_Label4 = Label(tab2, text="White Balance:")
Tab2_Label4.grid(row=3)

Tab2_Label5 = Label(tab2, text="Shooting interval:")
Tab2_Label5.grid(row=4)
Tab2_Entry1 = Entry(tab2)
Tab2_Entry1.grid(row=4, column=1)



#VideoProducer
Tab3_Label1 = Label(tab3, text="Frames per second:")
Tab3_Label1.grid(row=0)
Tab3_Entry1 = Entry(tab3)
Tab3_Entry1.grid(row=0, column=1)

#add the time lapse code here
def TimeLapse():
    print("The Timelapse Video")

Tab3_button1 =Button (tab3, text="Produce the video",command=TimeLapse)
Tab3_button1.grid(row=1,column=0)




window.mainloop()
