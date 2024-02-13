import customtkinter
from api import Detector
from api2 import Detector
import sys
import cv2
import easygui

# define parameters, apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# GUI
root = customtkinter.CTk()
root.geometry("800x550")

def camera():
    print("Turning on Camera..")
    
    source = "rtsp://user:test1234@192.168.1.101:8554/profile0"      
    cap = cv2.VideoCapture(source)

    while cap.isOpened():
        ret, frame = cap.read()

        # Initialize detector
        detector = Detector(model_name='rapid',
                            weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                            use_cuda=False)
        
        # A simple example to run on a single image and plt.imshow() it
        detector.detect_one(img_path=frame,
                            input_size=1024, conf_thres=0.3,
                            visualize=True)


        cv2.imshow('video', frame)

        if cv2.waitKey(20) == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def screenshot():
    print("Taking Screenshot...")
    source = "rtsp://user:test1234@192.168.1.101:8554/profile0"   
    cap=cv2.VideoCapture(source)
    ret, frame=cap.read()
    cv2.imwrite("frame.jpg", frame)
    print("=== Screenshot has been taken! ===")

def rapid():
    # Initialize detector
    detector = Detector(model_name='rapid',
                        weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                        use_cuda=False)

    read_img = easygui.fileopenbox(filetypes=["*.jpg","*.jpeg","*.png"])
    
    # A simple example to run on a single image and plt.imshow() it
    detector.detect_imgSeq(img_path=read_img,
                        input_size=1024, conf_thres=0.3,
                        visualize=True)
    
def rapidfa():
    # Initialize detector
    detector = Detector(model_name='rapid',
                        weights_path='./weights/RAPiD_FA.ckpt',
                        use_cuda=False)
    
    read_img = easygui.fileopenbox(filetypes=["*.jpg","*.jpeg","*.png"])

    # A simple example to run on a single image and plt.imshow() it
    detector.detect_one(img_path=read_img,
                        input_size=1024, conf_thres=0.3,
                        visualize=True)

def rapidfgfa():
    # Initialize detector
    detector = Detector(model_name='rapid',
                        weights_path='./weights/RAPiD_FGFA.ckpt',
                        use_cuda=False)

    read_img = easygui.fileopenbox(filetypes=["*.jpg","*.jpeg","*.png"])

    # A simple example to run on a single image and plt.imshow() it
    detector.detect_one(img_path=read_img,
                        input_size=1024, conf_thres=0.3,
                        visualize=True)

def leave():
    sys.exit()


# Add Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Welcome", font=("Helvetica", 50))
label.pack(pady=12, padx=10)

# Button text font
custom_font = ("Helvetica",20)

openCameraBtn = customtkinter.CTkButton(master=frame, text="Open Camera", command=camera, height=50, width=220, font=custom_font, hover_color="green", corner_radius=40)
openCameraBtn.pack(pady=12, padx=10)

ssBtn = customtkinter.CTkButton(master=frame, text="Take Screenshot", command=screenshot, height=50, width=220, font=custom_font, hover_color="green", corner_radius=40)
ssBtn.pack(pady=12, padx=10)

rapidBtn = customtkinter.CTkButton(master=frame, text="RAPID Image", command=rapid, height=50, width=220, font=custom_font, hover_color="green", corner_radius=40)
rapidBtn.pack(pady=12, padx=10)

faBtn = customtkinter.CTkButton(master=frame, text="RAPID-FA Image", command=rapidfa, height=50, width=220, font=custom_font, hover_color="green", corner_radius=40)
faBtn.pack(pady=12, padx=10)

fgfaBtn = customtkinter.CTkButton(master=frame, text="RAPID-FGFA Image", command=rapidfgfa, height=50, width=120, font=custom_font, hover_color="green", corner_radius=40)
fgfaBtn.pack(pady=12, padx=10)

exitBtn = customtkinter.CTkButton(master=frame, text="Exit", command=leave, height=50, width=230, font=custom_font, hover_color="green", corner_radius=40)
exitBtn.pack(pady=12, padx=10)

root.mainloop()