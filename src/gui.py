import tkinter as tk
from tkinter import filedialog, messagebox
from file_utils import organise_files

def launch_app():
    global path_entry
    root = tk.Tk()
    root.title("Automated File Organiser")

    
    input_frame = tk.Frame(root, padx=10, pady=10)
    input_frame.pack(fill="x")

    tk.Label(input_frame, text="Pick a folder:").pack(side="left", padx=5)
    path_entry = tk.Entry(input_frame, width=40)
    path_entry.pack(side="left", padx=5)

    def browse_folder():
        folder_selected = filedialog.askdirectory(title="Select a folder")
        if folder_selected:
            path_entry.delete(0, tk.END)
            path_entry.insert(0, folder_selected)

    def start_organising():
        folder = path_entry.get()
        if folder:
            organise_files(folder) 
            messagebox.showinfo("Success", f"Files in {folder} have been organised!")
        else:
            messagebox.showwarning("No Folder", "Please select a folder first!")

    browse_button = tk.Button(input_frame, text="Browse", command=browse_folder)
    browse_button.pack(side="left", padx=5)

    
    action_frame = tk.Frame(root, padx=10, pady=10)
    action_frame.pack(fill="x")

    start_button = tk.Button(action_frame, text="Start Organising", command=start_organising)
    start_button.pack(side="left", padx=5)

    exit_button = tk.Button(action_frame, text="Exit", command=root.quit)
    exit_button.pack(side="left", padx=5)

    root.mainloop()
