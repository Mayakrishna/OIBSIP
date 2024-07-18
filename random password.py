import random
import string
import tkinter as tk
from tkinter import messagebox

# Define character sets
letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Invalid password length")
        return

    character_pool = ''
    if letters_var.get():
        character_pool += letters
    if digits_var.get():
        character_pool += digits
    if symbols_var.get():
        character_pool += symbols

    if not character_pool:
        messagebox.showerror("Error", "No character types selected")
        return

    password = ''.join(random.choice(character_pool) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x250")

# Create and place widgets for user input and options
length_label = tk.Label(root, text="Password Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

letters_var = tk.BooleanVar(value=True)
digits_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

letters_check = tk.Checkbutton(root, text="Include Letters", variable=letters_var)
letters_check.pack()

digits_check = tk.Checkbutton(root, text="Include Digits", variable=digits_var)
digits_check.pack()

symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

password_entry = tk.Entry(root, width=30)
password_entry.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Run the application
root.mainloop()
