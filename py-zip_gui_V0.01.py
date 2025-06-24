from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from zipfile import ZipFile
import os
import sys

# Make the GUI DPI aware for crisp display on high-DPI screens
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


root = Tk()
root.title("Py-Zip")
root.geometry("400x200")
root.configure(bg="#283746")

# Set the corner icon
try:    # Check if running as a PyInstaller bundle
    if getattr(sys, 'frozen', False):
        # Running as a bundle
        bundle_dir = sys._MEIPASS
        icon_path = os.path.join(bundle_dir, "Py-Zipicon2.ico")
    else:
        # Running as a script
        icon_path = "Py-Zipicon2.ico"
    
    # For .ico files, use iconbitmap instead of PhotoImage
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Could not load icon: {e}")
    # Continue without icon if loading fails

file_var = StringVar()      # Variable to hold the file path
output_var = StringVar()    # Variable to hold the output folder path

def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("all files", "*.*"), ("Text files", "*.txt*"))
    )
    if filename:
        file_var.set(filename)  # Set the entry box to the selected file path

def browse_output_folder():
    foldername = filedialog.askdirectory(
        initialdir="/",
        title="Select Output Folder"
    )
    if foldername:
        output_var.set(foldername)  # Set the entry box to the selected folder path

######### Zip and Unzip Functions #########
def zip_file():
    file_path = file_var.get()
    output_folder = output_var.get()
    
    if not file_path:
        print("Please select a file to zip")
        return
    
    if not output_folder:
        print("Please select an output folder")
        return
      # Get the filename without path and extension for the zip name
    filename = os.path.basename(file_path)
    zip_name = os.path.splitext(filename)[0] + '.zip'
    zip_path = os.path.join(output_folder, zip_name)
    
    try:
        with ZipFile(zip_path, 'w') as zipf:
            zipf.write(file_path, filename)
        print(f"Successfully zipped {filename} to {zip_path}")
    except Exception as e:
        print(f"Error zipping file: {e}")


def unzip_file():
    zip_path = file_var.get()
    extract_path = output_var.get()
    
    if not zip_path:
        print("Please select a zip file to extract")
        return
    
    if not extract_path:
        print("Please select an output folder")
        return
    
    try:
        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Successfully extracted {zip_path} to {extract_path}")
    except Exception as e:
        print(f"Error extracting file: {e}")


########File Select#######

frm = ttk.Frame(root, padding=8)
frm.pack(pady=20)

entry = ttk.Entry(frm, textvariable=file_var, width=40)
entry.grid(column=0, row=1, columnspan=3, padx=5)

browse_button = ttk.Button(frm, text="Browse Files", command=browse_file)
browse_button.grid(column=3, row=1, pady=5)

########Output Selection#####

output_entry = ttk.Entry(frm, textvariable=output_var, width=40)
output_entry.grid(column=0, row=2, columnspan=3, padx=5)

output_button = ttk.Button(frm, text="Output Folder", command=browse_output_folder)
output_button.grid(column=3, row=2, pady=5)

zipfile = ttk.Button(frm, padding=5, text="Zip File", command=zip_file)
zipfile.grid(column=0, row=3, pady=10, padx=5)

unzipfile = ttk.Button(frm, padding=5, text="Unzip File", command=unzip_file)
unzipfile.grid(column=1, row=3, pady=10, padx=5)

root.mainloop()