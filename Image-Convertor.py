import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

root = tk.Tk()
root.title("Image Converter")
root.geometry("600x440")
root.configure(bg='azure3')


def getPNG():
    global im1
    import_file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if import_file_path:
        im1 = Image.open(import_file_path)
        messagebox.showinfo("Success", "PNG file loaded successfully!")
        convert_button.config(state=tk.NORMAL)  

# Function to convert and save the image as JPG
def convert():
    global im1
    if im1:
        export_file_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG files", "*.jpg")])
        if export_file_path:
            im1.save(export_file_path)
            messagebox.showinfo("Success", "Image converted and saved successfully!")
            download_button.config(state=tk.NORMAL) 
            
# Function to  download the converted image
def download():
    messagebox.showinfo("Download", "JPG file is ready for download!")

label1 = tk.Label(root, text="Image Converter", bg='azure3', font=('helvetica', 20))
label1.pack(pady=20)

browse_png = tk.Button(root, text="Select PNG file", command=getPNG, bg="royalblue", fg='white', font=('helvetica', 12, 'bold'))
browse_png.pack(pady=10)

convert_button = tk.Button(root, text="Convert PNG to JPG", command=convert, bg='royalblue', fg='white', font=('helvetica', 12, 'bold'), state=tk.DISABLED)
convert_button.pack(pady=10)

download_button = tk.Button(root, text="Download JPG", command=download, bg='green', fg='white', font=('helvetica', 12, 'bold'), state=tk.DISABLED)
download_button.pack(pady=10)

root.mainloop()