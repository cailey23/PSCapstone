print("1 Recommendation Frame Rate (24fps) Calculator")
print("2 Customized Frame Rate Calculator")

choice = input("Which one do you want to use : ")

clip_length = float(input("Enter Clip Length : "))
event_duration = float(input("Enter Event Duration: "))
image_size = float(input("Enter Image Size: "))

if choice == "1":
    print("Shooting Interval in second :",(event_duration/clip_length/24))
    print("Number of Images :", (clip_length*24))
    print("Storage Use :",(clip_length*24*image_size))

elif choice == "2":
    frame_rate = float(input("Enter Frame Per Second: "))
    print("Shooting Interval in second: ",(event_duration/clip_length/frame_rate))
    print("Number of Images :", (clip_length*frame_rate))
    print("Storage Use :", (clip_length*frame_rate*image_size))