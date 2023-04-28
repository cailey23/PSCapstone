import cv2
from PIL import Image,ImageTk
from tkinter import ttk

def capture_preview_image():
    # Create a VideoCapture object to capture frames from the camera
    cap = cv2.VideoCapture(0)

    # Check if the camera was successfully opened
    if not cap.isOpened():
        print("Error opening video stream or file")

    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was successfully captured
    if ret:
        # Save the frame as an image file
        cv2.imwrite("captured_image.jpg", frame)

    # Release the VideoCapture object
    cap.release()
    return True

def display_preview_image(window):
    # Open the image file using PIL
    image = Image.open("captured_image.jpg")

    # Convert the PIL image into a Tkinter-compatible PhotoImage object
    photo = ImageTk.PhotoImage(image)

    # Create a Tkinter label and display the PhotoImage
    preview_label = ttk.Label(window, image=photo)
    preview_label.grid(row=2, column=4)