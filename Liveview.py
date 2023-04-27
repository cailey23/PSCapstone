import cv2 as cv2

Liveview=cv2.VideoCapture (1)

while True:
    ret,frame=Liveview.read()

    if ret==True:
        cv2.imshow("Liveview",frame)
        key=cv2.waitKey(1)
        if key==ord("q"):
            break

Liveview.release()
cv2.destroyAllWindows()


        
