import tkinter as tk
from tkinter import filedialog, messagebox
import logging
from mbox_to_pst import convert_mbox_to_pst

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

def browse_mbox_file():
    file_path = filedialog.askopenfilename(title="Select MBOX File", filetypes=[("MBOX Files", "*.mbox")])
    mbox_file_entry.delete(0, tk.END)
    mbox_file_entry.insert(0, file_path)

def browse_pst_file():
    file_path = filedialog.asksaveasfilename(title="Save as PST File", defaultextension=".pst", filetypes=[("PST Files", "*.pst")])
    pst_file_entry.delete(0, tk.END)
    pst_file_entry.insert(0, file_path)

def convert():
    mbox_file = mbox_file_entry.get()
    pst_file = pst_file_entry.get()

    if not mbox_file or not pst_file:
        messagebox.showerror("Error", "Please provide both MBOX and PST file paths.")
        return

    try:
        convert_mbox_to_pst(mbox_file, pst_file)
        messagebox.showinfo("Success", f"Conversion completed successfully!\nPST saved as: {pst_file}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

# Set up the GUI window
root = tk.Tk()
root.title("MBOX to PST Converter")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

# MBOX file selection
mbox_file_label = tk.Label(frame, text="Select MBOX file:")
mbox_file_label.grid(row=0, column=0, sticky="w")
mbox_file_entry = tk.Entry(frame, width=40)
mbox_file_entry.grid(row=0, column=1)
browse_mbox_button = tk.Button(frame, text="Browse", command=browse_mbox_file)
browse_mbox_button.grid(row=0, column=2)

# PST file selection
pst_file_label = tk.Label(frame, text="Save as PST file:")
pst_file_label.grid(row=1, column=0, sticky="w")
pst_file_entry = tk.Entry(frame, width=40)
pst_file_entry.grid(row=1, column=1)
browse_pst_button = tk.Button(frame, text="Browse", command=browse_pst_file)
browse_pst_button.grid(row=1, column=2)

# Convert button
convert_button = tk.Button(frame, text="Convert", command=convert)
convert_button.grid(row=2, columnspan=3, pady=10)

root.mainloop()
