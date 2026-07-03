import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x200")

# Function to display the greeting
def greet():
    name = name_entry.get()

    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")
    else:
        messagebox.showwarning("Input Error", "Enter your name.")

# Create a label
name_label = tk.Label(root, text="Enter your name:")
name_label.pack(pady=10)

# Create an entry box
name_entry = tk.Entry(root)
name_entry.pack(pady=10)

# Create a button
greet_button = tk.Button(root, text="Greet", command=greet)
greet_button.pack(pady=10)

# Start the application
root.mainloop()      