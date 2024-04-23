import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os
import subprocess
import string
import threading as th
import qrcode
import time
import datetime

def create_qr_code():
    # If target save folder does not exist, create it
    if not os.path.exists("QR-codes"):
        os.makedirs("QR-codes")

    # Create QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
    )
    img = qr.make_image(fill_color=code_color.get(), back_color=background_color.get())

    # Get timestamp
    ts = time.time()
    date_string = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S-%f')
    date_string = date_string.replace(':', '-')

    # Give image a name and save it
    image_name_string = "QR-codes/QR-" + date_string + ".png"
    img.save(image_name_string)

    # Replace image with the newly created QR code image
    image = Image.open(image_name_string)
    image = ImageOps.fit(image, (300, 300))
    image = ImageTk.PhotoImage(image)
    image_area.configure(image=image)
    image_area.image = image

    # Change status text
    status_text = "QR created with name: " + "QR-" + date_string + ".png"
    content_label.configure(text=status_text)

# Create window, set size and window title
window = tk.Tk()
window.title("Parrot QR Creator")
window.geometry("450x700")
window.iconbitmap("res/parrot-icon.ico")

# Image file
image = Image.open("res/placeholder-image.jpg")
image = ImageOps.fit(image, (300, 300))
image = ImageTk.PhotoImage(image)

# Empty space
empty_label = tk.Label(window, text="")
empty_label.pack(side="top", pady=1)

# Input text
content_label = tk.Label(window, text="Text to embed:", font=('Arial', 13), height = 1)
content_label.pack(side="top", pady=5, padx=10)
content_field = tk.Entry(window, width=50)
content_field.pack(side="top",)

# Code color option
code_color_label = tk.Label(window, text="Code color:", font=('Arial', 13), height = 1)
code_color_label.pack(side="top", pady=5)
code_color_options = ["black", "white", "grey", "red", "crimson", "blue", "cyan", "green", "palegreen", "olive", "yellow", "gold", "orange", "chocolate", "brown", "pink", "violet", "purple"]
code_color = tk.StringVar()
code_color.set(code_color_options[0])
code_color_dropdown = tk.OptionMenu(window, code_color, *code_color_options)
code_color_dropdown.pack()

# Background color option
background_color_label = tk.Label(window, text="Background color:", font=('Arial', 13), height = 1)
background_color_label.pack(side="top", pady=5)
background_color_options = ["white", "black", "grey", "red", "crimson", "blue", "cyan", "green", "palegreen", "olive", "yellow", "gold", "orange", "chocolate", "brown", "pink", "violet", "purple"]
background_color = tk.StringVar()
background_color.set(background_color_options[0])
background_color_dropdown = tk.OptionMenu(window, background_color, *background_color_options)
background_color_dropdown.pack()

# Start button
start_button = tk.Button(window, text="Create QR code", font=('Arial', 14), command=lambda: th.Thread(target=create_qr_code).start(), height = 1, width = 15)
start_button.pack(side="top", pady=20)

# Latest QR code or placeholder image
image_area = tk.Label(window, image = image, bg="#11a3a7")
image_area.pack(side="top", pady=10)

# Label for newest image
content_label = tk.Label(window, text="", font=('Arial', 13), wraplength=300, height = 3)
content_label.pack(side="top", pady=5)

# Start process
window.mainloop()
