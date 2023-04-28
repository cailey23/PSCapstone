from typing import Tuple
import tkinter as tk
from tkinter import BOTTOM, TOP, StringVar, ttk
#from Timelapse import TimeLapse
from capture_images import start_capture
from camera_control import *
from PIL import Image,ImageTk
from capture_test_image import *

def begin_timelapse(frequency_s: int, num_images:int, image_folder:str, fps:int, resolution: Tuple[int,int]):
    get_images, is_finished = start_capture(frequency_s=frequency_s, num_images=num_images,
                                            image_folder=image_folder)
    TimeLapse(get_images, is_finished, fps=fps, resolution=resolution)

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.shutter_speed = tk.StringVar()
        self.aperture = tk.StringVar()
        self.iso = tk.StringVar()
        self.whitebalance = tk.StringVar()

        self.videolength_result = tk.StringVar()
        self.totalnumberofphotos_result = tk.StringVar()
        self.captureinterval_entry = tk.StringVar()

        self.show_preview_image_flag = False

        # creating a container
        container = tk.Frame(self, width=1024, height=570)
        container.grid(row=0,column=0)
        # container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting of the different page layouts
        for F in (StartPage, CameraSettingPage, CalculatorPage, VideoLength, CaptureInterval, ReviewPage):
            frame = F(container, self)

            # initializing frame of that object from below pages for loop
            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def set_shutter_speed(self, value):
        print("change shutterspeed to: " + value)
        self.shutter_speed.set("Shutter Speed: " + value)
        set_config_entry("shutterspeed", value)

    def set_aperture(self, value):
        self.aperture.set("Aperture:         " + value)
        set_config_entry("f-number", value)


    def set_iso(self, value):
        self.iso.set("ISO:                  " + value)
        set_config_entry("iso", value)

    def set_whitebalance(self, value):
        self.whitebalance.set("Whitebalance:  " + value)
        set_config_entry("whitebalance", value)

    def set_videolength(self, value):
        self.videolength_result.set("Video Length in minutes: " + value)

    def set_totalnumberofphotos(self, value):
        self.totalnumberofphotos_result.set("Total Number of Images: " + value)

    def set_captureinterval_entry(self, value):
        self.captureinterval_entry.set("Capture Interval in seconds: " + value)
    
    def show_preview_image_flag(self):
        self.show_preview_image_flag = True

# Startpage
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Welcome", font=('Arial',50))
        label.grid(row=0,column=0,padx=400, pady=100)

        # Create a style for the button
        style = ttk.Style()
        style.configure('my.TButton', width=20, height=50)

        button1 = ttk.Button(self, text="Next",style='my.TButton',
                             command=lambda: controller.show_frame(CameraSettingPage))


        # Button
        button1.grid(row=1,column=0,pady=100)


# Camera Setting Page
class CameraSettingPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Camera Setting", font=('Arial',35))
        label.grid(row=0, column=2, padx=20, pady=60)
        
        exposuremode = ttk.Label(self,text="Exposure Mode is: " + get_config_entry("expprogram"),font=('Arial',15))
        exposuremode.grid(row=1,column=2, padx=20)

        shutterspeed = ttk.Label(self, text="Shutter Speed:",font=('Arial',15))
        shutterspeed.grid(row=2,column=0, padx=20)
        shutterspeed_course = ["--", "1/2", "1/4", "1/8", "1/15", "1/30", "1/60", "1/125", "1/250", "1/500", "1/1000"]
        shutterspeed_cmb = ttk.Combobox(self, value=shutterspeed_course, width=10)
        shutterspeed_cmb.grid(row=2, column=1, padx=20)

        aperture = ttk.Label(self, text="Aperture:",font=('Arial',15))
        aperture.grid(row=3)
        aperture_course = ["--", "1.4", "2", "2.8", "4", "5.6", "8", "11", "16", "22"]
        aperture_cmb = ttk.Combobox(self, value=aperture_course, width=10)

        shutterspeed_cmb.set('--')
        aperture_cmb.set('--')

        controller.set_shutter_speed(shutterspeed_cmb.get())
        controller.set_aperture(aperture_cmb.get())

        shutterspeed_cmb.bind("<<ComboboxSelected>>", lambda event: controller.set_shutter_speed(shutterspeed_cmb.get()))
        aperture_cmb.grid(row=3, column=1)
        aperture_cmb.bind("<<ComboboxSelected>>", lambda event: controller.set_aperture(aperture_cmb.get()))
        cameraISO = ttk.Label(self, text="ISO:",font=('Arial',15))
        cameraISO.grid(row=4)
        cameraISO_course = ["--","50","100","125","160", "200","250","320","400","500","640","800","1000","1250","1600","2000","2500","3200","4000","5000","6400"]
        cameraISO_cmb = ttk.Combobox(self, value=cameraISO_course, width=10)
        cameraISO_cmb.grid(row=4, column=1)

        whitebalance = ttk.Label(self, text="White Balance:",font=('Arial',15))
        whitebalance.grid(row=5)
        whitebalance_course = ["--", "Natural light auto", "Direct sunlight", "Cloudy", "Shade", "Incandescent",
                               "Fluorescent"]
        whitebalance_cmb = ttk.Combobox(self, value=whitebalance_course, width=10)
        whitebalance_cmb.grid(row=5, column=1)

        cameraISO_cmb.set('--')
        whitebalance_cmb.set('--')

        controller.set_iso(cameraISO_cmb.get())
        controller.set_whitebalance(whitebalance_cmb.get())

        cameraISO_cmb.bind("<<ComboboxSelected>>",
                              lambda event: controller.set_iso(cameraISO_cmb.get()))

        whitebalance_cmb.bind("<<ComboboxSelected>>", lambda event: controller.set_whitebalance(whitebalance_cmb.get()))

        def display_preview_image():
            # Open the image file using PIL
            image = Image.open("captured_image.jpg")

            # Resize the image to a width of 300 pixels while preserving aspect ratio
            width, height = image.size
            aspect_ratio = height / width
            resized_width = 300
            resized_height = int(resized_width * aspect_ratio)
            resized_image = image.resize((resized_width, resized_height), Image.ANTIALIAS)

            # Convert the PIL image into a Tkinter-compatible PhotoImage object
            photo = ImageTk.PhotoImage(resized_image)

            # Create a Tkinter label and display the PhotoImage
            preview_label = ttk.Label(self, image=photo)
            preview_label.image = photo
            preview_label.grid(row=1, column=4)         

        # buttons
        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(StartPage))

        button1.grid(row=6, column=1, padx=10, pady=30)

        button2 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(CalculatorPage))

        button2.grid(row=6, column=5, padx=10, pady=30)

        button3 = ttk.Button(self, text="Capture Preview Image",
                             command=lambda: [capture_preview_image(),display_preview_image()])

        button3.grid(row=3, column=2)

# Calculator Page
class CalculatorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Calculator",font=('Arial',35))
        label.grid(row=0, column=2, padx=30, pady=30)

        button1 = ttk.Button(self, text="Calculate Video Length",
                             command=lambda: controller.show_frame(VideoLength))

        button1.grid(row=1, column=1, padx=30, pady=30)

        button2 = ttk.Button(self, text="Calculate Capture Interval",
                             command=lambda: controller.show_frame(CaptureInterval))

        button2.grid(row=1, column=4, padx=30, pady=30)

        button3 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(CameraSettingPage))

        button3.grid(row=10, column=0, padx=30, pady=250)

        button4 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(ReviewPage))

        button4.grid(row=10, column=5, padx=15, pady=250)


# Video Length Frame
class VideoLength(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Video Length Calculator",font=('Arial',35))
        label.grid(row=0, column=1, padx=10, pady=10)

        # Enter Value
        videoframerate = ttk.Label(self, text="Video Frame Rate:",font=('Arial',15))
        videoframerate.grid(row=1,column=0,padx=40)
        videoframerate_course = ["6", "12", "15", "24", "30"]
        videoframerate_cmb = ttk.Combobox(self, value=videoframerate_course, width=30)
        videoframerate_cmb.grid(row=1, column=1)

        eventlength = ttk.Label(self, text="Event Length in hours:",font=('Arial',15))
        eventlength.grid(row=2)
        ELvalue = StringVar()
        eventlength_entry = ttk.Entry(self, textvariable=ELvalue)
        eventlength_entry.grid(row=2, column=1)

        captureinterval = ttk.Label(self, text="Capture Interval in seconds:",font=('Arial',15))
        captureinterval.grid(row=3)
        CIvalue = StringVar()
        captureinterval_entry = ttk.Entry(self, textvariable=CIvalue)
        captureinterval_entry.grid(row=3, column=1)

        # Calculation
        def Cal_videolength():
            controller.set_captureinterval_entry(str(CIvalue.get()))
            EL = int(ELvalue.get())
            CI = int(CIvalue.get())
            FPS = int(videoframerate_cmb.get())
            videolength = (EL * 3600 / (FPS * CI))
            videolength_in_min = round(videolength / 60, 2)
            numberofphotos = (videolength * FPS)
            videolength_result = ttk.Label(self, text=f"{videolength_in_min}")
            videolength_result.grid(row=5, column=1)
            controller.set_videolength(str(videolength_in_min))
            totalnumberofphotos_result = ttk.Label(self, text=f"{numberofphotos}")
            totalnumberofphotos_result.grid(row=6, column=1)
            controller.set_totalnumberofphotos(str(numberofphotos))

        # Result
        videolength = ttk.Label(self, text="Video Length in minutes:",font=('Arial',15))
        videolength.grid(row=5)

        imagenumber = ttk.Label(self, text="Total Number of Images:",font=('Arial',15))
        imagenumber.grid(row=6)
        # Tab1_labelresult2= Label(text=f"{numberofphotos}")

        # buttons
        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(CalculatorPage))

        button1.grid(row=7, column=0, padx=10, pady=10)

        button2 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(ReviewPage))

        button2.grid(row=7, column=5, padx=10, pady=10)


        button3 = ttk.Button(self, text="Calculate",
                             command=Cal_videolength)

        button3.grid(row=4, column=1, padx=10, pady=10)


# Capture Interval Frame
class CaptureInterval(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Capture Interval Calculator",font=('Arial',35))
        label.grid(row=0, column=1, padx=10, pady=10)

        # Enter Value
        videoframerate = ttk.Label(self, text="Video Frame Rate:",font=('Arial',15))
        videoframerate.grid(row=1)
        videoframerate_course = ["6", "12", "15", "24", "30"]
        videoframerate_cmb = ttk.Combobox(self, value=videoframerate_course, width=30)
        videoframerate_cmb.grid(row=1, column=1)

        eventlength = ttk.Label(self, text="Event Length in hours:",font=('Arial',15))
        eventlength.grid(row=2)
        ELvalue = StringVar()
        eventlength_entry = ttk.Entry(self, textvariable=ELvalue)
        eventlength_entry.grid(row=2, column=1)

        videolength = ttk.Label(self, text="Video Length in minutes:",font=('Arial',15))
        videolength.grid(row=3)
        VLvalue = StringVar()
        videolength_entry = ttk.Entry(self, textvariable=VLvalue)
        videolength_entry.grid(row=3, column=1)

        # Calculation
        def Cal_captureinterval():
            controller.set_videolength(str(VLvalue.get()))
            EL = int(ELvalue.get())
            VL = int(VLvalue.get())
            FPS = int(videoframerate_cmb.get())
            captureinterval = round(EL * 3600 / (VL * 60 * FPS))
            numberofphotos = (VL *60* FPS)
            captureinterval_result = ttk.Label(self, text=f"{captureinterval}")
            captureinterval_result.grid(row=5, column=1)
            controller.set_captureinterval_entry(str(captureinterval))
            totalnumberofphotos_result = ttk.Label(self, text=f"{numberofphotos}")
            totalnumberofphotos_result.grid(row=6, column=1)
            controller.set_totalnumberofphotos(str(numberofphotos))

        # Result
        captureinterval = ttk.Label(self, text="Capture Interval in seconds:",font=('Arial',15))
        captureinterval.grid(row=5)

        imagenumber = ttk.Label(self, text="Total Number of Images:",font=('Arial',15))
        imagenumber.grid(row=6)

        # Button
        button1 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(CalculatorPage))

        button1.grid(row=7, column=0, padx=10, pady=10)

        button2 = ttk.Button(self, text="Next",
                             command=lambda: controller.show_frame(ReviewPage))

        button2.grid(row=7, column=5, padx=10, pady=10)

        button3 = ttk.Button(self, text="Calculate",
                             command=Cal_captureinterval)

        button3.grid(row=4, column=1, padx=10, pady=10)


# Review Page
class ReviewPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        title = ttk.Label(self, text="Review",font=('Arial',35))
        title.grid(row=0, column=2, padx=30, pady=10)
        lowertitle1 = ttk.Label(self, text="Camera Settings",font=('Arial',25))
        lowertitle1.grid(row=2, column=0, padx=7, pady=10)
        lowertitle2 = ttk.Label(self, text="Time Lapse Settings",font=('Arial',25))
        lowertitle2.grid(row=2, column=4, padx=7, pady=10)

        # Review Camera Settings
        shutterspeed = ttk.Label(self, textvariable=controller.shutter_speed,font=('Arial',15))
        shutterspeed.grid(row=3)

        aperture = ttk.Label(self, textvariable=controller.aperture,font=('Arial',15))
        aperture.grid(row=4)

        cameraISO = ttk.Label(self, textvariable=controller.iso,font=('Arial',15))
        cameraISO.grid(row=5)

        whitebalance = ttk.Label(self, textvariable=controller.whitebalance,font=('Arial',15))
        whitebalance.grid(row=6)

        # Review Calculator Results
        # captureinterval = ttk.Label(self, text="Capture Interval in seconds:")
        captureinterval = ttk.Label(self, textvariable=controller.captureinterval_entry,font=('Arial',15))
        captureinterval.grid(row=3, column=4)

        # numberofimage = ttk.Label(self, text="Total Number of Images:")
        numberofimage = ttk.Label(self, textvariable=controller.totalnumberofphotos_result,font=('Arial',15))
        numberofimage.grid(row=4, column=4)

        # videolength = ttk.Label(self, text="Video Length in minutes")
        videolength = ttk.Label(self, textvariable=controller.videolength_result,font=('Arial',15))
        videolength.grid(row=5, column=4)

        # Buttons
        button1 = ttk.Button(self, text="Edit",
                             command=lambda: controller.show_frame(CameraSettingPage))

        button1.grid(row=8, column=1, padx=7, pady=60)

        button2 = ttk.Button(self, text="Edit",
                             command=lambda: controller.show_frame(CalculatorPage))

        button2.grid(row=8, column=4, padx=7, pady=60)

        button3 = ttk.Button(self, text="Back",
                             command=lambda: controller.show_frame(CalculatorPage))

        button3.grid(row=11, column=0, padx=7, pady=60)

        button4 = ttk.Button(self, text="Begin",
                             command= lambda: begin_timelapse(frequency_s=float(controller.captureinterval_entry.get().split(" ")[-1]),
                                                              num_images=int(float(controller.totalnumberofphotos_result.get().split(" ")[-1])),
                                                              image_folder="/media/root/T7/Images",
                                                              fps=float(controller.totalnumberofphotos_result.get().split(" ")[-1])/float(controller.videolength_result.get().split(" ")[-1])/60,
                                                              resolution=(3840, 2160)))
        button4.grid(row=11, column=5, padx=7, pady=60)

# Driver Code
app = tkinterApp()
app.geometry("1024x570")
app.title("TimeLapse")
app.mainloop()
