import customtkinter
from api import Detector


# define parameters, apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# GUI
root = customtkinter.CTk()
root.geometry("500x350")

def viewimages():
    # Initialize detector
    detector = Detector(model_name='rapid',
                        weights_path='./weights/pL1_MWHB1024_Mar11_4000.ckpt',
                        use_cuda=False)

    # A simple example to run on a single image and plt.imshow() it
    detector.detect_one(img_path='./images/exhibition.jpg',
                        input_size=1024, conf_thres=0.3,
                        visualize=True)
    
def camera():
    print("You have chosen to Open Camera.")


# Add Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="User Interface")
label.pack(pady=12, padx=10)

openCamera = customtkinter.CTkButton(master=frame, text="Open Camera", command=camera)
openCamera.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Image", command=viewimages)
button.pack(pady=12, padx=10)

root.mainloop()