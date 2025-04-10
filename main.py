import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import scrolledtext
from mbox_to_pst import mbox_to_pst
import os

class MboxToPstApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MBox to PST Converter")
        self.root.geometry("500x400")
        
        # Set up the layout
        self.create_widgets()

    def create_widgets(self):
        # MBox file selection
        self.mbox_label = tk.Label(self.root, text="Select MBOX File:")
        self.mbox_label.pack(pady=5)
        self.mbox_button = tk.Button(self.root, text="Browse...", command=self.browse_mbox)
        self.mbox_button.pack(pady=5)
        self.mbox_file = tk.Entry(self.root, width=50)
        self.mbox_file.pack(pady=5)

        # PST output file selection
        self.pst_label = tk.Label(self.root, text="Select Output PST File:")
        self.pst_label.pack(pady=5)
        self.pst_button = tk.Button(self.root, text="Browse...", command=self.browse_pst)
        self.pst_button.pack(pady=5)
        self.pst_file = tk.Entry(self.root, width=50)
        self.pst_file.pack(pady=5)

        # Convert button
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_mbox)
        self.convert_button.pack(pady=20)

        # Log output area
        self.log_area = scrolledtext.ScrolledText(self.root, width=60, height=10, wrap=tk.WORD)
        self.log_area.pack(pady=10)
        self.log_area.config(state=tk.DISABLED)

    def browse_mbox(self):
        mbox_path = filedialog.askopenfilename(filetypes=[("MBOX Files", "*.mbox")])
        if mbox_path:
            self.mbox_file.delete(0, tk.END)
            self.mbox_file.insert(0, mbox_path)

    def browse_pst(self):
        pst_path = filedialog.asksaveasfilename(defaultextension=".pst", filetypes=[("PST Files", "*.pst")])
        if pst_path:
            self.pst_file.delete(0, tk.END)
            self.pst_file.insert(0, pst_path)

    def convert_mbox(self):
        mbox_file = self.mbox_file.get()
        pst_file = self.pst_file.get()

        # Basic validation
        if not mbox_file or not pst_file:
            messagebox.showerror("Error", "Please provide both MBOX and PST files.")
            return
        
        # Log the start of the conversion
        self.log_message(f"Starting conversion from {mbox_file} to {pst_file}...")
        
        # Call the conversion function
        try:
            mbox_to_pst(mbox_file, pst_file)
            self.log_message("Conversion successful!")
            messagebox.showinfo("Success", "Conversion completed successfully!")
        except Exception as e:
            self.log_message(f"Error: {str(e)}")
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def log_message(self, message):
        """Log messages in the GUI output area."""
        self.log_area.config(state=tk.NORMAL)
        self.log_area.insert(tk.END, message + "\n")
        self.log_area.config(state=tk.DISABLED)
        self.log_area.yview(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = MboxToPstApp(root)
    root.mainloop()
