import tkinter as tk
from PIL import Image, ImageTk, ImageOps
import os
import subprocess
import string
import threading as th
import qrcode as qr
import time
import datetime

def create_qr_code():
    # Create QR code
    img = qr.make(content_field.get())

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
    status_text = "QR created with name: " + image_name_string
    content_label.configure(text=status_text)

# Create window, set size and window title
window = tk.Tk()
window.title("Parrot QR Creator")
window.geometry("400x600")

# Image file
image = Image.open("res/placeholder-image.jpg")
image = ImageOps.fit(image, (300, 300))
image = ImageTk.PhotoImage(image)

# Input text
content_label = tk.Label(window, text="Text to embed:", font=('Arial', 15), height = 1)
content_label.pack(side="top", pady=20)
content_field = tk.Entry(window, width=50)
content_field.pack(side="top",)

# Start button
start_button = tk.Button(window, text="Create QR code", font=('Arial', 15), command=lambda: th.Thread(target=create_qr_code).start(), height = 1, width = 15)
start_button.pack(side="top", pady=20)

# Latest QR code or placeholder image
image_area = tk.Label(window, image = image, bg="#11a3a7")
image_area.pack(side="top", pady=10)

# Label for newest image
content_label = tk.Label(window, text="", font=('Arial', 13), wraplength=300, height = 3)
content_label.pack(side="top", pady=5)

# Start process
window.mainloop()
