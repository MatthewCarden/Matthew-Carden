# Matthew Carden
# Assignment P2
# GUI Development Spring 2025

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Constants for tax rates
FICA_RATE = 0.0765
FEDERAL_RATE = 0.22
STATE_RATE = 0.04

def compute_taxes():
    """Compute the tax deductions and net pay based on biweekly gross income."""
    try:
        # Get user input and convert to float
        gross_income = float(entry_income.get())
        
        # Compute taxes
        fica_tax = gross_income * FICA_RATE
        federal_tax = gross_income * FEDERAL_RATE
        state_tax = gross_income * STATE_RATE
        net_income = gross_income - (fica_tax + federal_tax + state_tax)
        
        # Display results formatted as currency
        label_fica_value.config(text=f"${fica_tax:,.2f}")
        label_federal_value.config(text=f"${federal_tax:,.2f}")
        label_state_value.config(text=f"${state_tax:,.2f}")
        label_net_income.config(text=f"Net Paycheck Income: ${net_income:,.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for gross income.")
        entry_income.delete(0, tk.END)
        entry_income.focus()

def clear_fields():
    """Clear all input and output fields."""
    entry_income.delete(0, tk.END)
    label_fica_value.config(text="")
    label_federal_value.config(text="")
    label_state_value.config(text="")
    label_net_income.config(text="Net Paycheck Income:")
    entry_income.focus()

def exit_app():
    """Exit the application."""
    root.quit()

# Create main application window
root = tk.Tk()
root.title("Payroll Calculator")
root.geometry("700x550")  
root.configure(bg="white")

# Load and display the payroll image
image_path = "payroll.jpg"
try:
    image = Image.open(image_path)
    image = image.resize((250, 150), Image.LANCZOS)  # Increased image size
    photo = ImageTk.PhotoImage(image)
    label_image = tk.Label(root, image=photo, bg="white")
    label_image.image = photo  # Keep a reference to prevent garbage collection
    label_image.place(x=20, y=20)  # Position at the top-left
except Exception as e:
    print("Error loading image:", e)

# Titles
tk.Label(root, text="Payroll Calculator", font=("Arial", 22, "bold"), bg="white", fg="black").place(x=420, y=40)
tk.Label(root, text="Paycheck Calculation", font=("Arial", 18), bg="white", fg="black").place(x=420, y=80)

# Input Section
tk.Label(root, text="Enter Gross Pay:", font=("Arial", 16), bg="white", fg="black").place(x=160, y=200)
entry_income = tk.Entry(root, font=("Arial", 16), fg="white", bg="black")
entry_income.place(x=300, y=200, width=180)

# Buttons
frame_buttons = tk.Frame(root, bg="white")
frame_buttons.place(x=160, y=250)

btn_compute = tk.Button(frame_buttons, text="Compute Taxes", font=("Arial", 14), command=compute_taxes)
btn_compute.grid(row=0, column=0, padx=15)
btn_clear = tk.Button(frame_buttons, text="Clear", font=("Arial", 14), command=clear_fields)
btn_clear.grid(row=0, column=1, padx=15)
btn_exit = tk.Button(frame_buttons, text="Exit", font=("Arial", 14), command=exit_app)
btn_exit.grid(row=0, column=2, padx=15)

# Tax Output Section
frame_output = tk.Frame(root, bg="white")
frame_output.place(x=160, y=320)

tk.Label(frame_output, text="FICA:", font=("Arial", 16), bg="white", fg="black").grid(row=0, column=0, padx=20, sticky="w")
tk.Label(frame_output, text="Federal Tax:", font=("Arial", 16), bg="white", fg="black").grid(row=0, column=1, padx=20, sticky="w")
tk.Label(frame_output, text="State Tax:", font=("Arial", 16), bg="white", fg="black").grid(row=0, column=2, padx=20, sticky="w")

label_fica_value = tk.Label(frame_output, text="", font=("Arial", 16), bg="white", fg="black")
label_fica_value.grid(row=1, column=0, padx=20, sticky="w")
label_federal_value = tk.Label(frame_output, text="", font=("Arial", 16), bg="white", fg="black")
label_federal_value.grid(row=1, column=1, padx=20, sticky="w")
label_state_value = tk.Label(frame_output, text="", font=("Arial", 16), bg="white", fg="black")
label_state_value.grid(row=1, column=2, padx=20, sticky="w")

label_net_income = tk.Label(root, text="Net Paycheck Income:", font=("Arial", 18, "bold"), bg="white", fg="black")
label_net_income.place(x=230, y=420)

# Run the application
root.mainloop()

