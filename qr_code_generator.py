
import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk


# Main application window
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("500x650")
root.configure(bg="#eaf2f8")
root.resizable(False, False)

qr_image = None
qr_photo = None


# Generate QR Code function
def generate_qr():

    global qr_image, qr_photo

    data = entry.get().strip()

    if data == "":
        messagebox.showerror("Error", "Please enter text or URL!")
        return

    try:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4
        )

        qr.add_data(data)
        qr.make(fit=True)

        qr_image = qr.make_image(
            fill_color="black",
            back_color="white"
        ).convert("RGB")

        # Display QR Code
        display_image = qr_image.resize((250, 250))
        qr_photo = ImageTk.PhotoImage(display_image)

        qr_label.config(image=qr_photo, text="")

        messagebox.showinfo(
            "Success",
            "QR Code generated successfully!"
        )

    except Exception as e:
        messagebox.showerror("Error", str(e))


# Save QR Code function
def save_qr():

    if qr_image is None:
        messagebox.showerror(
            "Error",
            "Please generate a QR Code first!"
        )
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG Image", "*.png")],
        initialfile="my_qrcode.png"
    )

    if file_path:
        qr_image.save(file_path)

        messagebox.showinfo(
            "Saved",
            "QR Code saved successfully!"
        )


# Application heading
heading = tk.Label(
    root,
    text="QR CODE GENERATOR",
    font=("Arial", 22, "bold"),
    bg="#eaf2f8",
    fg="#154360"
)
heading.pack(pady=25)


# Instructions
instruction = tk.Label(
    root,
    text="Enter text or website URL below",
    font=("Arial", 12),
    bg="#eaf2f8"
)
instruction.pack(pady=10)


# Input box
entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=35,
    bd=2
)
entry.pack(pady=15)


# Generate button
generate_button = tk.Button(
    root,
    text="Generate QR Code",
    font=("Arial", 12, "bold"),
    bg="#2874a6",
    fg="white",
    width=22,
    command=generate_qr
)
generate_button.pack(pady=15)


# QR Code display area
qr_label = tk.Label(
    root,
    text="QR Code will appear here",
    font=("Arial", 12),
    bg="white",
    width=30,
    height=12
)
qr_label.pack(pady=20)


# Save button
save_button = tk.Button(
    root,
    text="Save QR Code",
    font=("Arial", 12, "bold"),
    bg="#239b56",
    fg="white",
    width=22,
    command=save_qr
)
save_button.pack(pady=15)


# Footer
footer = tk.Label(
    root,
    text="Developed using Python and Tkinter",
    font=("Arial", 10),
    bg="#eaf2f8",
    fg="#566573"
)
footer.pack(side="bottom", pady=15)


# Run application
root.mainloop()
