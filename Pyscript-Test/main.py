import customtkinter
import cv2
import easygui
import sys

# define parameters, apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# GUI
root = customtkinter.CTk()
root.geometry("500x350")

def viewimages():
    print("You have chosen view Images.")
    
def camera():
    print("You have chosen to Open Camera.")

def leave():
    sys.exit()


# Add Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome")
label.pack(pady=12, padx=10)

openCameraBtn = customtkinter.CTkButton(master=frame, text="Open Camera", command=camera)
openCameraBtn.pack(pady=12, padx=10)

imageBtn = customtkinter.CTkButton(master=frame, text="Image", command=viewimages)
imageBtn.pack(pady=12, padx=10)

exitBtn = customtkinter.CTkButton(master=frame, text="Exit", command=leave)
exitBtn.pack(pady=12, padx=10)

root.mainloop()