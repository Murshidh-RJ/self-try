import qrcode
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

def generate_qr():
    data = url_entry.get().strip()
    if not data:
        messagebox.showerror("Input Error", "Please enter a valid URL or text!")
        return
    
    try:
        filename = filedialog.asksaveasfilename(defaultextension=".png", 
                                                filetypes=[("PNG files", "*.png")])
        if not filename:
            return  # User cancelled the save dialog

        qr = qrcode.QRCode(border=4, box_size=10)
        qr.add_data(data)
        qr.make(fit=True)
        image = qr.make_image(fill_color="black", back_color="white")
        image.save(filename)

        # Display QR code in the GUI
        img = Image.open(filename)
        img = img.resize((200, 200))  # Resize for display
        qr_img = ImageTk.PhotoImage(img)
        qr_label.config(image=qr_img)
        qr_label.image = qr_img
        url_display_label.config(text=f"URL: {data}")
        
        messagebox.showinfo("Success", f"QR code saved as {filename}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# URL input field
tk.Label(root, text="Enter URL or text:").pack(pady=5)
url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Generate button
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=10)

# QR code image display
qr_label = tk.Label(root)
qr_label.pack(pady=10)

# URL display label
url_display_label = tk.Label(root, text="")
url_display_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
