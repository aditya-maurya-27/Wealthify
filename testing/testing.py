import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image, ImageTk

def generate_qr():
    url = entry.get().strip()
    if not url:
        messagebox.showerror("Error", "Enter a valid URL")
        return
    qr = qrcode.QRCode(box_size=9, border=1)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#ee8319", back_color="#3f3f3f")  # Customize colors
    qr_photo = ImageTk.PhotoImage(img)
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo

root = tk.Tk()
root.title("QR Generator")
entry = tk.Entry(root, font="Arial 14", width=30)
entry.pack(pady=10)
tk.Button(root, text="Generate", command=generate_qr).pack(pady=10)
qr_label = tk.Label(root)
qr_label.pack(pady=20)
root.mainloop()
