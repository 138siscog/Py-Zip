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
folder_var = StringVar()    # Variable to hold the folder path
output_var = StringVar()    # Variable to hold the output folder path

def browse_file():
    filename = filedialog.askopenfilename(
        initialdir="/",
        title="Select a File",
        filetypes=(("all files", "*.*"), ("Text files", "*.txt*"))
    )
    if filename:
        file_var.set(filename)  # Set the entry box to the selected file path

def browse_folder():
    foldername = filedialog.askdirectory(
        initialdir="/",
        title="Select a Folder"
    )
    if foldername:
        folder_var.set(foldername)  # Set the entry box to the selected folder path

def browse_output_folder():
    # Default to Desktop as the initial location
    desktop = os.path.join(os.path.expanduser("~"), "Desktop")
    foldername = filedialog.askdirectory(
        initialdir=desktop,
        title="Select Output Folder"
    )
    if foldername:
        output_var.set(foldername)  # Set the entry box to the selected folder path

######### Zip and Unzip Functions #########

def folder_zip():
    folder_path = folder_var.get()
    output_folder = output_var.get()

    if not folder_path or not os.path.isdir(folder_path):
        print("Please select a valid folder to zip")
        return

    if not output_folder:
        print("Please select an output folder")
        return

    # Get the folder name for the zip file
    folder_name = os.path.basename(os.path.normpath(folder_path))
    zip_name = folder_name + '.zip'
    zip_path = os.path.join(output_folder, zip_name)

    try:
        with ZipFile(zip_path, 'w') as zipf:
            for root_dir, dirs, files in os.walk(folder_path):
                for file in files:
                    abs_file = os.path.join(root_dir, file)
                    rel_path = os.path.relpath(abs_file, folder_path)
                    zipf.write(abs_file, rel_path)
        print(f"Successfully zipped folder {folder_name} to {zip_path}")
    except Exception as e:
        print(f"Error zipping folder: {e}")


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


########File/Folder Select#######

frm = ttk.Frame(root, padding=8)
frm.pack(pady=20)

# File selection widgets
file_entry = ttk.Entry(frm, textvariable=file_var, width=40)
file_entry.grid(column=0, row=1, columnspan=2, padx=5)
file_button = ttk.Button(frm, text="Browse File", command=browse_file)
file_button.grid(column=2, row=1, pady=5)
zipfile_btn = ttk.Button(frm, padding=5, text="Zip File", command=zip_file)
zipfile_btn.grid(column=1, row=4, pady=0, padx=0)

# Folder selection widgets
folder_entry = ttk.Entry(frm, textvariable=folder_var, width=40)
folder_entry.grid(column=0, row=2, columnspan=2, padx=5)
folder_button = ttk.Button(frm, text="Browse Folder", command=browse_folder)
folder_button.grid(column=2, row=2, pady=5)
zipfolder_btn = ttk.Button(frm, padding=5, text="Zip Folder", command=folder_zip)
zipfolder_btn.grid(column=2, row=4, pady=5, padx=3)

# Output folder selection
output_entry = ttk.Entry(frm, textvariable=output_var, width=40)
output_entry.grid(column=0, row=3, columnspan=2, padx=5)
output_button = ttk.Button(frm, text="Output Folder", command=browse_output_folder)
output_button.grid(column=2, row=3, pady=5)

# Unzip button (uses file_var for zip file path)
unzipfile_btn = ttk.Button(frm, padding=5, text="Unzip File", command=unzip_file)
unzipfile_btn.grid(column=0, row=4, pady=0, padx=3)

root.mainloop()