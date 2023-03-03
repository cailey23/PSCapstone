import tkinter as tk
from tkinter import BOTTOM, TOP, StringVar, ttk



class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        
        # creating a container
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, CameraSettingPage, CalculatorPage, VideoLength, CaptureInterval, ReviewPage):

            frame = F(container, self)

            # initializing frame of that object from below pages for loop
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

#Startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Welcome" )
        label.pack(side=TOP)

        button1 = ttk.Button(self, text ="Next",
        command = lambda : controller.show_frame(CameraSettingPage))
        
        #Button
        button1.pack(side=BOTTOM)

        

        


#Camera Setting Page
class CameraSettingPage(tk.Frame):

    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Camera Setting")
        label.grid(row = 0, column = 2, padx = 10, pady = 10)
        
        shutterspeed = ttk.Label(self, text="Shutter Speed:")
        shutterspeed.grid(row=1)
        shutterspeed_course = ["Auto","1/2","1/4","1/8","1/15","1/30","1/60","1/125","1/250","1/500","1/1000"]
        shutterspeed_cmb = ttk.Combobox(self,value=shutterspeed_course, width=10)
        shutterspeed_cmb.grid(row=1, column=1)
        
        

        aperture = ttk.Label(self, text="Aperture:")
        aperture.grid(row=2)
        aperture_course = ["Auto","1.4","2","2.8","4","5.6","8","11","16","22"]
        aperture_cmb = ttk.Combobox(self,value=aperture_course , width=10)
        aperture_cmb.grid(row=2, column=1)

        cameraISO = ttk.Label(self, text="ISO:")
        cameraISO.grid(row=3)
        cameraISO_course = ["Auto","50","100","200","400","800","1600","3200","6400"]
        cameraISO_cmb = ttk.Combobox(self,value=cameraISO_course, width=10)
        cameraISO_cmb.grid(row=3, column=1)

        whitebalance = ttk.Label(self, text="White Balance:")
        whitebalance.grid(row=4)
        whitebalance_course = ["Auto","Natural light auto","Direct sunlight","Cloudy","Shade","Incandescent","Fluorescent"]
        whitebalance_cmb = ttk.Combobox(self,value=whitebalance_course, width=10)
        whitebalance_cmb.grid(row=4, column=1)


        #buttons
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(StartPage))
    
        button1.grid(row = 7, column = 0, padx = 10, pady = 10)


        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(CalculatorPage))
    
        button2.grid(row = 7, column = 5, padx = 10, pady = 10)




#Calculator Page
class CalculatorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Calculator")
        label.grid(row = 0, column = 2, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Calculate Video Length",
                            command = lambda : controller.show_frame(VideoLength))
    
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Calculate Capture Interval",
                            command = lambda : controller.show_frame(CaptureInterval))
    
        button2.grid(row = 1, column = 4, padx = 10, pady = 10)

    
        button3 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(CameraSettingPage))
    
        button3.grid(row = 2, column = 0, padx = 10, pady = 10)

       
        button4 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(ReviewPage))
    
        button4.grid(row = 2, column = 5, padx = 10, pady = 10)

#Video Length Frame
class VideoLength (tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Video Length Calculator")
        label.grid (row = 0, column = 1, padx = 10, pady = 10)

        #Enter Value
        videoframerate = ttk.Label(self, text="Video Frame Rate:")
        videoframerate.grid(row=1)
        videoframerate_course = ["6","12","15","24","30"]
        videoframerate_cmb = ttk.Combobox (self, value=videoframerate_course, width=30)
        videoframerate_cmb.grid(row=1, column=1)

        eventlength = ttk.Label(self, text="Event Length in hours:")
        eventlength.grid(row=2)
        ELvalue = StringVar()
        eventlength_entry = ttk.Entry(self,textvariable=ELvalue)
        eventlength_entry.grid(row=2, column=1)

        captureinterval = ttk.Label(self, text="Capture Interval in seconds:")
        captureinterval.grid(row=3)
        CIvalue = StringVar()
        captureinterval_entry = ttk.Entry(self, textvariable=CIvalue)
        captureinterval_entry.grid(row=3, column=1)

        #Calculation
        def Cal_videolength(self):
         EL = int(ELvalue.get())
         CI = int(CIvalue.get())
         FPS = int(videoframerate_cmb.get())
         videolength = (EL*3600/(FPS*CI))
         videolength_in_min = (videolength/60)
         numberofphotos = (videolength*FPS)
         videolength_result= ttk.Label(text=f"{videolength_in_min}")
         videolength_result.grid(row=5, column=1)
         totalnumberofphotos_result= ttk.Label(text=f"{numberofphotos}")
         totalnumberofphotos_result.grid(row=6, column=1)

        #Result
        videolength = ttk.Label(self, text="Video Length in minutes:")
        videolength.grid(row=5)
        
        imagenumber = ttk.Label(self, text="Total Number of Images:")
        imagenumber.grid(row=6)
        #Tab1_labelresult2= Label(text=f"{numberofphotos}")

        #buttons
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(CalculatorPage))
    
        button1.grid(row = 7, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(ReviewPage))
    
        button2.grid(row = 7, column = 5, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Calculate",
                            command = Cal_videolength)
    
        button3.grid(row = 4, column = 1, padx = 10, pady = 10)
        

#Capture Interval Frame
class CaptureInterval (tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)
        label = ttk.Label(self, text="Capture Interval Calculator")
        label.grid (row = 0, column = 1, padx = 10, pady = 10)

        #Enter Value
        videoframerate = ttk.Label(self, text="Video Frame Rate:")
        videoframerate.grid(row=1)
        videoframerate_course = ["6","12","15","24","30"]
        videoframerate_cmb = ttk.Combobox (self, value=videoframerate_course, width=30)
        videoframerate_cmb.grid(row=1, column=1)

        eventlength = ttk.Label(self, text="Event Length in hours:")
        eventlength.grid(row=2)
        ELvalue = StringVar()
        eventlength_entry = ttk.Entry(self,textvariable=ELvalue)
        eventlength_entry.grid(row=2, column=1)

        videolength = ttk.Label(self, text="Video Length in minutes:")
        videolength.grid(row=3)
        VLvalue = StringVar()
        videolength_entry = ttk.Entry(self,textvariable=VLvalue)
        videolength_entry.grid(row=3, column=1)

        #Calculation
        def Cal_captureinterval(self):
         EL = int(ELvalue.get())
         VL = int(VLvalue.get())
         FPS = int(videoframerate_cmb.get())
         captureinterval = (EL*3600/(VL*60*FPS))
         numberofphotos = (VL*FPS)
         captureinterval_result= ttk.Label(text=f"{captureinterval}")
         captureinterval_result.grid(row=5, column=1)
         totalnumberofphotos_result= ttk.Label(text=f"{numberofphotos}")
         totalnumberofphotos_result.grid(row=6, column=1)

        #Result
        captureinterval = ttk.Label(self, text="Capture Interval in seconds:")
        captureinterval.grid(row=5)

        imagenumber = ttk.Label(self, text="Total Number of Images:")
        imagenumber.grid(row=6)

        #Button
        button1 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(CalculatorPage))
    
        button1.grid(row = 7, column = 0, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Next",
                            command = lambda : controller.show_frame(ReviewPage))
    
        button2.grid(row = 7, column = 5, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Calculate",
                            command = Cal_captureinterval)
    
        button3.grid(row = 4, column = 1, padx = 10, pady = 10)
       
        




# Review Page
class ReviewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = ttk.Label(self, text ="Review")
        title.grid(row = 0, column = 2, padx = 10, pady = 10)
        lowertitle1 = ttk.Label(self, text ="Camera Settings")
        lowertitle1.grid(row = 1, column = 0, padx = 10, pady = 10)
        lowertitle2 = ttk.Label(self, text ="Time Lapse Settings")
        lowertitle2.grid(row = 1, column = 4, padx = 10, pady = 10)
        
        #Review Camera Settings
        shutterspeed = ttk.Label(self, text="Shutter Speed:")
        shutterspeed.grid(row=2)
    
        aperture = ttk.Label(self, text="Aperture:")
        aperture.grid(row=3)
       
        cameraISO = ttk.Label(self, text="ISO:")
        cameraISO.grid(row=4)
        
        whitebalance = ttk.Label(self, text="White Balance:")
        whitebalance.grid(row=5)

        #Review Calculator Results
        captureinterval = ttk.Label(self, text="Capture Interval in seconds:")
        captureinterval.grid(row=2,column=4)

        numberofimage = ttk.Label(self, text="Capture Interval in seconds:")
        numberofimage.grid(row=3,column=4)

        videolength = ttk.Label(self, text="Capture Interval in seconds:")
        videolength.grid(row=4,column=4)

        #Buttons
        button1 = ttk.Button(self, text ="Edit",
                            command = lambda : controller.show_frame(CameraSettingPage))

        button1.grid(row = 6, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Edit",
                            command = lambda : controller.show_frame(CalculatorPage))

        button2.grid(row = 6, column = 4, padx = 10, pady = 10)

        button3 = ttk.Button(self, text ="Back",
                            command = lambda : controller.show_frame(CalculatorPage))

        button3.grid(row = 7, column = 0, padx = 10, pady = 10)


        button4 = ttk.Button(self, text ="Begin")
        button4.grid(row = 7, column = 5, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
