import tkinter as tk
import sys


def on_button_click():
    print("Button clicked!")


def on_close_click(root):
    print("Close button clicked!")
    root.destroy()


def run_gui():
    root = tk.Tk()
    root.title("Simple Tkinter Example")
    tk.Label(root, text="Hello, Tkinter!").pack()
    tk.Button(root, text="Close", command=lambda: on_close_click(root)).pack()
    tk.Button(root, text="Click me!", command=on_button_click).pack()
    root.mainloop()


run_gui()
