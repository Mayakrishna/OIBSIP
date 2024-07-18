import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Function to calculate BMI
def calculate_bmi(weight, height):
    """Calculate BMI given weight in kilograms and height in meters."""
    return weight / (height ** 2)

# Function to determine BMI category
def get_bmi_category(bmi):
    """Return the BMI category for a given BMI value."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

# Function to get current date and time
def get_date_time():
    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

# Function to calculate BMI from GUI input
def calculate_bmi_gui():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get())

        if unit_var.get() == "Imperial":
            weight = weight * 0.453592  # Convert pounds to kilograms
            height = height * 0.0254  # Convert inches to meters

        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        date_time = get_date_time()

        result_text.set(f"Your BMI is: {bmi:.2f}\nYou are categorized as: {category}\nCurrent Date and Time: {date_time}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Create StringVar to update the result label
result_text = tk.StringVar()
unit_var = tk.StringVar(value="Metric")

# Create and place labels and entry widgets
tk.Label(root, text="Weight:").grid(row=0, column=0, padx=10, pady=10)
entry_weight = tk.Entry(root)
entry_weight.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Height:").grid(row=1, column=0, padx=10, pady=10)
entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Create radio buttons for unit selection
tk.Radiobutton(root, text="Metric (kg/m)", variable=unit_var, value="Metric").grid(row=2, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Imperial (lb/in)", variable=unit_var, value="Imperial").grid(row=2, column=1, padx=10, pady=5)

# Create and place calculate button
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi_gui)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# Create and place result label
result_label = tk.Label(root, textvariable=result_text, font=("Helvetica", 16), justify="center")
result_label.grid(row=4, column=0, columnspan=2, pady=20, sticky ="nsew")

# Center the label within the grid
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Configure weight for other rows and columns to ensure centering
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(5, weight=1)

# Run the main loop
root.mainloop()

# Console-based BMI Calculator
def main_console():
    print("Welcome to the BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are categorized as: {category}")
        print(f"Current Date and Time: {get_date_time()}")
    except ValueError:
        print("Invalid input. Please enter numerical")
