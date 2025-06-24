# Py-Zip GUI - File Compressor & Extractor (WIP)

**Py-Zip** Python-based alternative to WinRAR and 7-Zip. It features a user-friendly graphical interface built with **Tkinter**, allowing you to compress and decompress files easily. This project is evolving to include advanced features like folder zipping and batch operations.

---

## Name Change from Zippy to Py-Zip ##

## Current Features

- Graphical user interface built with **Tkinter**
- File browser for selecting files to compress or decompress
- Output folder selector
- **Compress files** into `.zip` format with a single click
- **Decompress .zip** files into a folder
- Corner app icon (`Py-Zip icon.png`)
- Custom background color (`#283746` navy tone)
- Automatic zip file naming based on selected file
- DPI awareness on high-resolution displays (Windows)

---

## ❌ Features Not Yet Implemented

| Feature                         | Status       | Notes                                                               |
|--------------------------------|---------------|---------------------------------------------------------------------|
| Compress entire folders        | 🔜 Planned   | Currently only supports single file compression                      |
| Multi-file selection           | ❌ Missing   | CLI version supported it, GUI version does not yet                   |
| Custom zip file naming         | ❌ Missing   | Zip name is auto-generated from filename                             |
| GUI user feedback (popups)     | ❌ Missing   | Uses print statements; needs Tkinter messageboxes for success/errors |
| Drag and drop support          | ❌ Missing   | Future usability improvement                                         |

---

## 🛠 How to Run

```bash
python zip_gui_V0.01.py
