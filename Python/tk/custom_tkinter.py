from customtkinter import *
from PIL import Image

app = CTk()
app.geometry("500x400")
set_appearance_mode("dark")
"""
btn = CTkButton(master=app, text="Click Me", corner_radius=32, fg_color="transparent",
                hover_color="#4158D0", border_color="#FFCC70", border_width=2, image=CTkImage(dark_image=img, light_image=img))
label = CTkLabel(master=app, text="Some Text...", font=("Arial", 20), text_color="#FFCC70")

label.place(relx=0.5, rely=0.5, anchor="center")
"""
combobox = CTkComboBox(master=app, values=["Option 1","Option 2", "Option 3"],fg_color="#0093E9",
                dropdown_fg_color="#0093E9", border_color="#FFCC70")
combobox.place(relx=0.5, rely=0.5, anchor="center")
app.mainloop()