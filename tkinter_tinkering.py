import tkinter as tk
from tkinter import filedialog  # Import the filedialog module
import sys
import eyed3  # Import the eyed3 library


def on_button_click():
    print("Button clicked!")


def on_close_click(root):
    print("Close button clicked!")
    root.destroy()


def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        print(f"Selected file: {file_path}")


def run_gui():
    root = tk.Tk()
    root.title("Simple Tkinter Example")
    tk.Label(root, text="Hello, Tkinter!").pack()
    tk.Button(root, text="Close", command=lambda: on_close_click(root)).pack()
    tk.Button(root, text="Click me!", command=on_button_click).pack()
    tk.Button(root, text="Open File", command=browse_file).pack()

    root.mainloop()


run_gui()
