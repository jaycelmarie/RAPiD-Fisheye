import customtkinter

# define parameters, apperance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# GUI
root = customtkinter.CTk()
root.geometry("500x350")

def gui():
    print("Test")


# Add Frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="User Interface")
label.pack(pady=12, padx=10)

button = customtkinter.CTkButton(master=frame, text="Image", command=gui)
button.pack(pady=12, padx=10)

root.mainloop()